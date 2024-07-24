from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

#Cocktail choices
COCKTAIL_TYPES = (
    ('sweet', 'Sweet'),
    ('sour', 'Sour'),
    ('strong', 'Strong'),
    ('zerozero', 'ZeroZero')
)

SPIRIT_TYPES = (
    ('vodka', 'Vodka'),
    ('whiskey', 'Whiskey'),
    ('rum', 'Rum'),
    ('gin', 'Gin'),
    ('liquor', 'Liquor')
)

class Recipe(models.Model):

    """
    Model to create and edit recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=400, null=False, blank=False)
    description = models.CharField(max_length=600, null=False, blank=False)
    instructions = RichTextField(max_length=12000, null=False, blank=False)
    ingredients = RichTextField(max_length=12000, null=False, blank=False)
    image = ResizedImageField(
        size=[350, None], quality=80, upload_to='recipes/', force_format='WEBP',
        blank=False, null=False
    )

    image_alt = models.CharField(max_length=200, null=False, blank=False)
    cocktail_type = models.CharField(max_length=100, choices=COCKTAIL_TYPES, default='sweet')
    spirit_types = models.CharField(max_length=100, choices=SPIRIT_TYPES, default='gin')
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.title)    
