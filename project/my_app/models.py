from django.db import models
from django.contrib.auth.models import User

class UserinfoModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    portfolio_site_model = models.URLField(blank=True)
    portfolio_pic_model = models.ImageField(upload_to ='profile_pics',blank=True)

    def __str__(self) -> str:
        return self.user.username