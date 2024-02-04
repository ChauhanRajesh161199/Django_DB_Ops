from django.db import models

# Create your models here.
class Pre_User(models.Model):
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Pre_User"

    def __str__(self):
        return f"{self.email} {self.created_at}"


class User(models.Model):
    userid = models.ForeignKey(Pre_User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "User"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"