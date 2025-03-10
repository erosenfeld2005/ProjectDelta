"""
Holds models of users
"""
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

#from project_delta.models import models

class CustomUser(AbstractUser):
    """
    Holds custom user data
    """
    name = models.CharField(max_length=150, blank=False, default="User")
    email = models.CharField(max_length=150, blank=False)
    isRestricted = models.BooleanField(default=False)

    #my_posts = models.ManyToManyField(Post, related_name="upvoted_posts", blank=True)
    #USE FOREIGN KEY... NOT ManyToMany 

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Ensure this is unique
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Ensure this is unique
        blank=True,
        verbose_name='user permissions',
    )
