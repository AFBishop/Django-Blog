from django.db import models

# Create your models here.


class Category(models.Model):
    item = models.CharField(verbose_name="类别", max_length=50)
    desc = models.CharField(verbose_name="描述", max_length=100)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item


class Django(models.Model):
    tittle = models.CharField(verbose_name="标题", max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category, verbose_name="类别")

    class Meta:
        verbose_name = "Django"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tittle


class Python(models.Model):
    tittle = models.CharField(verbose_name="标题", max_length=50)
    content = models.TextField(verbose_name="正文")
    category = models.ForeignKey(Category, verbose_name="类别")

    class Meta:
        verbose_name = "Python"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tittle
