from django.db import models
from .validators import real_age
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age, ))
    image = models.ImageField(
        'Фото', upload_to='birthday/', null=True, blank=True
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='unique_person_constraint',
            ),
        )

    def get_absolute_url(self):
        return reverse('birthday:detail', args=[str(self.pk)])