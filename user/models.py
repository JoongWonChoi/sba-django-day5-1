from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=64,verbose_name="User")
    useremail = models.EmailField(max_length = 128, verbose_name = "Email")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "가입일시")

    class Meta:
        verbose_name = "Users"

        verbose_name_plural = "Users"
