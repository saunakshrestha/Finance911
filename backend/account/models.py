import random
import string
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from finance911.logger import logger
from django.db.models.query import QuerySet
from django.utils import timezone

# Create your models here.
class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None, **other_fields):
        email = self.normalize_email(email)
        user  = self.model(email=email, username=username, **other_fields)
        if password is None:
            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            password=''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        user.set_password(password)
        user.save()
        return user
    
    # def create_supervisor(self, email, username, password=None, **other_fields):
    #     other_fields.setdefault('is_staff', False)
    #     other_fields.setdefault('is_superuser', False)
    #     other_fields.setdefault('is_active', False)

    #     user = self.create_user(email=email, username=username, password=password, **other_fields)
    #     groups = Group.objects.all()
    #     user.groups.add(*groups)
    #     return user
    
    def create_superuser(self, email, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is False:
            raise ValueError('Superuser must be assigned is_staff = True')

        if other_fields.get('is_superuser') is False:
            raise ValueError('Superuser must be assigned is_superuser = True')
        if not password:
            password=f'{username}@ekg'
        user = self.create_user(email=email, username=username, password=password, **other_fields)
        try:
            groups = Group.objects.all()
            user.groups.add(*groups)
        except Exception as e:
            logger.exception( stack_info=False,msg=e.args)
        return user
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


def location(instance,filename):
    return f'profile/{instance.username}/{filename}'
    
class Users(AbstractBaseUser, PermissionsMixin):
    profile_pic     = models.ImageField(verbose_name='Profile Image',default='profile/default_user.png', upload_to=location)
    email           = models.EmailField(verbose_name='Email', unique=True)
    username        = models.CharField(verbose_name='Username',max_length=255)
    ph_no           = models.CharField(verbose_name='Phone Number',max_length=20,unique=True)
    name            = models.CharField(verbose_name='Name',max_length=255, blank=True)
    is_active       = models.BooleanField(verbose_name='Active',default=False)
    is_staff        = models.BooleanField(verbose_name='Staff',default=False)
    is_superuser    = models.BooleanField(verbose_name='Superuser',default=False)
    date_joined     = models.DateField(verbose_name='date joined',auto_now_add=True,auto_now=False)
    updated         = models.DateTimeField(default=timezone.now)
    invalid_logins  = models.IntegerField(default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name','ph_no']

    objects = CustomAccountManager()

    def __str__(self):
        return f'{self.email}'

    def get_fullname(self):
        return f'{self.name}'

    def profile_pic_url(self):
        if self.profile_pic:
            return self.profile_pic.url
        return f"{settings.STATIC_URL}/assets_new/images/user.png"
    
    # def update_m2m(self,field_name,objs):
    #     remove_list = []
    #     try:
    #         if not isinstance(objs,list):
    #             objs = list(objs)
    #         field = getattr(self,field_name)
    #         for obj in field.all():
    #             if obj not in objs:
    #                 remove_list.append(obj)
    #             else:
    #                 objs.remove(obj)
    #         if remove_list:
    #             field.remove(*remove_list)
    #         if objs:
    #             field.add(*objs)
    #     except Exception as e:
    #         logger.exception(stack_info=False,msg=e.args)
    #     return remove_list,objs
    
    class Meta:
        db_table='users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

