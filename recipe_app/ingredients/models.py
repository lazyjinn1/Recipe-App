from django.db import models

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length = 20)
    pic = models.ImageField(upload_to='ingredients', default='no-picture.jpg')
    note = models.TextField(blank=True)

    def __str__(self):
        return str(self.ingredient_name)