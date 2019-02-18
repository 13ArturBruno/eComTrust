from django.db import models


class Category(models.Model):
    name = models.CharField('nome', max_length=60, blank=False, null=False)
    logo = models.ImageField('logo', upload_to='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
