from django.db import models

# Create your models here.

class Word(models.Model):

    content = models.CharField(max_length=50)

    accurates = models.ManyToManyField("Word", through="WordRelation", related_name="misspelleds")


    def get_accurates(self):
        
        ordered_accurates = self.accurates.all().order_by("-count")
        print(ordered_accurates)
    
    def __str__(self):

        return self.content[:30]


class WordRelation(models.Model):

    misspelled = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="rel_accurates")

    accurate = models.ForeignKey(Word, on_delete=models.CASCADE, related_name="rel_misspelleds")

    count = models.IntegerField(default=1)

    def __str__(self):

        return f"{self.misspelled.content[:30]},{self.accurate.content[:30]}, {self.count}"