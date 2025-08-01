from django.db import models

class CourtQuery(models.Model):
    case_type = models.CharField(max_length=20)
    case_number = models.CharField(max_length=20)
    filing_year = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    raw_html = models.TextField()
