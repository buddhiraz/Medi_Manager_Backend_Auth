from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    id  = models.AutoField(primary_key=True) 
    # user_id   = models.OneToOneField(User, on_delete=models.CASCADE)# ,to_field='username')
    # Email or Username will be enterd from Front-End
    first_name  = models.CharField(max_length=50 , blank = True)
    last_name   = models.CharField(max_length=50,blank=True)
    email       = models.EmailField(blank=True,unique=True)
    phone_number= models.CharField(max_length=10, blank = True)
    aadhar      = models.CharField(unique = True, 
                                   max_length=18,
                                   null=True,
                                   blank=True)
    # This will be modified to any Unique Num from ID card for citizens of other countries
    # Or We will give a drop down to select what kind of ID they are using 
    # Example - Voter ID , Aadhar , PAN etc

    address     = models.CharField(max_length=250,blank=True)
    postal_code = models.CharField(max_length=6 , 
                                   blank = True)

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
