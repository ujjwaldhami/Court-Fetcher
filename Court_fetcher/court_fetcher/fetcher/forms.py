from django import forms

COURT_CHOICES = [
    ('delhi', 'Delhi High Court'),
    ('bombay', 'Bombay High Court'),
]

class CourtSearchForm(forms.Form):
    court_name = forms.ChoiceField(choices=COURT_CHOICES, label='Court Name')
    case_type = forms.CharField(label='Case Type')
    case_number = forms.CharField(label='Case Number')
    filing_year = forms.IntegerField(label='Filing Year')
