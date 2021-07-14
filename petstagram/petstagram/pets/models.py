from django.db import models


class Pet(models.Model):

    def __str__(self):
        return f'{self.type} name: {self.name}'

    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot')
    )
    type = models.CharField(
        max_length=6,
        null=False,
        blank=False,
        choices=TYPE_CHOICES
    )
    name = models.CharField(
        max_length=6,
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        # validators=[
        #     models.Min(1)
        # ]
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    # image_url = models.URLField(
    #     null=False,
    #     blank=False,
    # )
    image = models.ImageField(
        upload_to='pets',
    )

class Like(models.Model):
    pet = models.ForeignKey(
        Pet,
        default=False,
        on_delete=models.CASCADE
    )
