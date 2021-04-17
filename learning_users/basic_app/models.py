from django.db import models
from django.contrib.auth.models import User

# importing admin wala user by using above cmd

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    # additional
    portfolio_site=models.URLField(blank=True)
    # as hmne media ko choose kra ha pics ko upload ke lia toh saara pics media ke age jo folder 
    # pass kra ha hmne wahan chli jainge 'profile_pics'
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username




