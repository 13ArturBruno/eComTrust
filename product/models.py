from django.db import models
from categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="categoria", on_delete=models.CASCADE)
    name = models.CharField('nome', max_length=60, blank=False, null=False)
    description = models.CharField('Descrição', max_length=150, blank=False, null=False)
    price = models.FloatField('Preço', null=False, blank=False, default=0.0)
    image = models.ImageField('imagem', upload_to='')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
