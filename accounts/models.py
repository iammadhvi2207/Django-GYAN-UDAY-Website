from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model — extended fully in Phase 2.
    Defined here in Phase 1 so AUTH_USER_MODEL works immediately.
    """

    ROLE_ADMIN   = 'admin'
    ROLE_FACULTY = 'faculty'
    ROLE_STUDENT = 'student'

    ROLE_CHOICES = [
        (ROLE_ADMIN,   'Admin'),
        (ROLE_FACULTY, 'Faculty'),
        (ROLE_STUDENT, 'Student'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_STUDENT,
    )

    # Phase 2 will add: phone, profile_picture, department, etc.

    def get_role_display_label(self):
        return dict(self.ROLE_CHOICES).get(self.role, 'User')

    def get_initials(self):
        parts = self.get_full_name().split()
        if len(parts) >= 2:
            return (parts[0][0] + parts[-1][0]).upper()
        return self.username[:2].upper()

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display_label()})"

