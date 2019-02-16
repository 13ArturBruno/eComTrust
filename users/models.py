from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    name = models.CharField('nome', max_length=60, blank=False, null=False)
    email = models.CharField('Email', max_length=100, blank=False)
    cpf = models.CharField('CPF', max_length=11, blank=True, null=True)
    is_seller = models.BooleanField('É Vendedor ??', blank=False, null=False, default=False)

