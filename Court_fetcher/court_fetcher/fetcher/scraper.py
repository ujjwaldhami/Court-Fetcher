def scrape_case_details(court_name, case_type, case_number, filing_year):
    if court_name == 'delhi':
        return run_delhi_scraper(case_type, case_number, filing_year)
    elif court_name == 'bombay':
        return run_bombay_scraper(case_type, case_number, filing_year)
    else:
        return {"error": "Unsupported court"}, ""

def run_delhi_scraper(case_type, case_number, filing_year):
    return {
        "court": "Delhi High Court",
        "case_type": case_type,
        "case_number": case_number,
        "filing_year": filing_year,
        "petitioner": "XYZ",
        "respondent": "ABC",
        "status": "Pending"
    }, "<html>raw_html</html>"

def run_bombay_scraper(case_type, case_number, filing_year):
    return {
        "court": "Bombay High Court",
        "case_type": case_type,
        "case_number": case_number,
        "filing_year": filing_year,
        "petitioner": "MNO",
        "respondent": "PQR",
        "status": "Disposed"
    }, "<html>raw_html</html>"
