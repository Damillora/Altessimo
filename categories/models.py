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
    def create_or_new(self, name):
        name = name.strip()
        qs = self.get_queryset().filter(name__iexact=name)
        if qs.exists():
            return qs.first(), False
        return Category.objects.create(name=name), True
    
    def comma_to_qs(self, categorys_str):
        final_ids = []
        for category in categories_str.split(','):
            obj, created = self.create_or_new(category)
            final_ids.append(obj.id)
        qs = self.get_queryset().filter(id__in=final_ids).distinct()
        return qs

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

