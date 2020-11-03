from django.db import models
from django.conf import settings
from .badge import Badge

class Profile(models.Model):
    name = models.CharField(max_length=30)
    #TODO: Use this as a container for bio and stats- assumed fields: tries, rates, reviews, entries, rep, description
    metadata = models.JSONField(null=True, blank=True)
    #TODO: Rather than modify user model from base, this can be used to store site configuration
    preferences = models.JSONField(null=True, blank=True)
    profile_pic = models.ImageField(blank=True, default="default.png")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #User can have no badges!
    badges = models.ManyToManyField("rameniaapp.Badge", blank=True)
    following = models.ManyToManyField("self",related_name="followers", symmetrical=False ,blank=True)

    def get_meta_val(self, key, alternative=None):
        if key in self.metadata:
            return self.metadata[key]
        else:
            return alternative

    def set_meta_val(self, key, val):
        self.metadata[key] = val
        self.save()
    
    def increment_meta_val(self, key, amount=1):
        old_val = self.get_meta_val(key, 0)
        self.set_meta_val(key, old_val + amount)
