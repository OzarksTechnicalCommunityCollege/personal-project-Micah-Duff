from django.db import models

class Size (models.TextChoices):
    UNIVERSAL = "UN", "Universal",
    XSMALL = "XS", "Extra Small",
    SMALL = "S", "Small",
    MEDIUM = "M", "Medium",
    LARGE = "L", "Large",
    XLARGE = "XL", "Extra Large"

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sizes = models.CharField(
        max_length=6,
        choices=Size.choices,
        default=Size.UNIVERSAL,
    )
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['sizes']),
        ]
    def __str__(self):
        return self.name
