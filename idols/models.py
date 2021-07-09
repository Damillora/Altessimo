from django.db import models

# Create your models here.

# Create your models here.


class IdolManager(models.Manager):
    def comma_to_qs(self, idols_str):
        final_ids = []
        if idols_str:
            for idol in idols_str.split(','):
                obj, created = self.get_or_create(romanized_name=idol.strip())
                final_ids.append(obj.id)
            qs = self.get_queryset().filter(id__in=final_ids).distinct()
            return qs
        return self.none()


class Idol(models.Model):
    branch = models.ForeignKey("categories.Branch", on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True)
    romanized_name = models.CharField(max_length=255)
    voice_actor_name = models.CharField(max_length=255, blank=True)
    romanized_voice_actor_name = models.CharField(max_length=255, blank=True)

    objects = IdolManager()

    class Meta:
        ordering = [ 'romanized_name','name' ]
    
    def __str__(self):
        return self.romanized_name+" "+"["+self.branch.acronym+"] "+" (CV: "+self.romanized_voice_actor_name+")"
