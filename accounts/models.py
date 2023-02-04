from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission


class Department(models.Model):
    """Model representing a department in the company"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """Meta class for Department model"""
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        """Return the string representation of a department"""
        return self.name


class Group(models.Model):
    """Model representing a group within a department"""
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """Meta class for Group model"""
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        """Return the string representation of a group"""
        return self.name


class UserManager(BaseUserManager):
    """Manager class for the User model"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model representing a user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='users_in_group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='users_with_permission',
        blank=True, help_text='Specific permissions for this user.'
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name
