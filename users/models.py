from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
HOST_GUEST_CHOICES = (
    (0, 'Guest'),
    (1, 'Host')
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, nickname, realname, phone_num, host_or_guest, address, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            nickname=nickname,
            realname=realname,
            phone_num=phone_num,
            host_or_guest=host_or_guest,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, nickname, realname, phone_num, host_or_guest, address, password):
        user = self.create_user(
            username=username,
            email=email,
            nickname=nickname,
            realname=realname,
            phone_num=phone_num,
            host_or_guest=host_or_guest,
            address=address,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    nickname = models.CharField(max_length=16)
    realname = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=20)
    host_or_guest = models.SmallIntegerField(choices=HOST_GUEST_CHOICES)
    address = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='user_image/%Y/%m/%d/', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'nickname',
        'realname',
        'phone_num',
        'host_or_guest',
        'address',
    ]

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser