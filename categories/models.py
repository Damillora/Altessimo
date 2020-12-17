from django.db import models
from django.utils.text import slugify

class Branch(models.Model):
    name = models.CharField(max_length=255,blank=True)
    acronym = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="logo",blank=True)

    def __str__(self):
        return self.name+" ["+self.acronym+"]"

# Create your models here.
class CategoryManager(models.Manager):
    def comma_to_qs(self, categories_str):
        final_ids = []
        if categories_str:
            for category in categories_str.split(','):
                obj, created = self.get_or_create(name=category.strip())
                final_ids.append(obj.id)
            qs = self.get_queryset().filter(id__in=final_ids).distinct()
            return qs
    return self.none()

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)

    objects = CategoryManager()

    class Meta:
        ordering = [ 'name' ]  
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

