from django.db import models
from django.conf import settings

class Report(models.Model):
    # Restrict choices for certain fields- format is 'stored value', 'readable value'
    REPORT_TYPE_CHOICES = [('RV', "Review"), ('PF', "Profile"), ('ND', "Noodle")]
    REASON_CHOICES = [('AD', "Advertising"), ('HR', "Harassment"), 
                    ('IC', "Copyrighted or illegal content"), 
                    ('GS', "Disgusting or disturbing content")]
    STATUS_CHOICES = [('OP', "Open"), ('ED', "Resolved"), ('SP', "Spam")]
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=REPORT_TYPE_CHOICES)
    reason = models.CharField(max_length=2, choices=REASON_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

# Django does not allow polymorphic relationships without external modules,
# so we just inherit
class ReviewReport(Report):
    review = models.ForeignKey("rameniaapp.Review", on_delete=models.CASCADE)

class ProfileReport(Report):
    profile = models.ForeignKey("rameniaapp.Profile", on_delete=models.CASCADE)

class NoodleReport(Report):
    noodle = models.ForeignKey("rameniaapp.Noodle", on_delete=models.CASCADE)
