from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=45)


class Food(models.Model):
    description = models.CharField(max_length=250)
    common_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    scientificname = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)


class Vitamins(models.Model):
    name = models.CharField(max_length=45)
    value_vit = models.ManyToManyField(Food, through="Value_Vitamins")


class Value_Vitamins(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False, blank=False)
    vitamins = models.ForeignKey(
        Vitamins, on_delete=models.CASCADE, null=False, blank=False
    )
    value = models.FloatField()


class Minerals(models.Model):
    name = models.CharField(max_length=50)
    value_min = models.ManyToManyField(Food, through="Value_Minerals")


class Value_Minerals(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False, blank=False)
    minerals = models.ForeignKey(
        Minerals, on_delete=models.CASCADE, null=False, blank=False
    )
    value = models.FloatField()


class PrincipalNutriments(models.Model):
    name = models.CharField(max_length=45)
    value_pri = models.ManyToManyField(Food, through="Value_PrincipalNutriments")


class Value_PrincipalNutriments(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False, blank=False)
    principalnutriments = models.ForeignKey(
        PrincipalNutriments, on_delete=models.CASCADE, null=False, blank=False
    )
    value = models.FloatField()
