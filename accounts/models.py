from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES =(
        ("Male", ("Male")),
        ("Female", ("Female"))
    )

    image = models.ImageField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    email = models.EmailField(('email adress'), unique=True, null=True)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, db_index=True, related_name='user', null=True)
    last_level_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Level(models.Model):
    title = models.CharField(max_length=50, default='0')
    selling_count = models.IntegerField(null=True)
    buying_count = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

    def __str__(self):
        return f'{self.title}'