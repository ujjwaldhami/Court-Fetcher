import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from .forms import CourtSearchForm
from .models import CourtQuery
from .scraper import scrape_case_details

def home(request):
    if request.method == 'GET' and 'court_name' in request.GET:
        form = CourtSearchForm(request.GET)
        if form.is_valid():
            court = form.cleaned_data['court_name']
            ctype = form.cleaned_data['case_type']
            number = form.cleaned_data['case_number']
            year = form.cleaned_data['filing_year']
            return redirect('fetch_case_details', court=court, ctype=ctype, number=number, year=year)
    else:
        form = CourtSearchForm()

    return render(request, 'fetcher/home.html', {'form': form})

def search(request, court, ctype, number, year):
    result, raw_html = scrape_case_details(court, ctype, number, year)

    CourtQuery.objects.create(
        case_type=ctype,
        case_number=number,
        filing_year=year,
        raw_html=raw_html
    )

    return render(request, 'fetcher/result.html', {'data': result})


def scrape_case_details(court, case_type, case_number, filing_year):
    if court.lower() != 'delhi':
        return {"error": "Only Delhi HC supported right now."}, ""

    session = requests.Session()
    url = "https://delhihighcourt.nic.in/case.asp"

    params = {
        "ctype": case_type,
        "cno": case_number,
        "cyear": filing_year,
        "submit": "Submit"
    }

    response = session.get(url, params=params)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    try:
        petitioner = soup.find('span', id='lblPet').text.strip()
        respondent = soup.find('span', id='lblRes').text.strip()
        filing_date = soup.find('span', id='lblFilingDate').text.strip()
        hearing_date = soup.find('span', id='lblNextDate').text.strip()

        pdf_links = soup.find_all('a', href=True)
        pdf_url = None
        for link in pdf_links:
            if 'pdf' in link['href'].lower():
                pdf_url = "https://delhihighcourt.nic.in" + link['href']
                break

        result = {
            'petitioner': petitioner,
            'respondent': respondent,
            'filing_date': filing_date,
            'hearing_date': hearing_date,
            'pdf_link': pdf_url or 'No PDF found'
        }

        return result, html

    except Exception as e:
        return {"error": "Case not found or parsing failed."}, html
