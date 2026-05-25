from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True,)

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category",args=[self.slug])
        
        

class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE,)

    title = models.CharField(max_length=255)

    slug = models.SlugField(max_length=255,unique=True,allow_unicode=True,)

    image = models.ImageField(upload_to="products/%Y/%m/%d/",blank=True,null=True,)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,decimal_places=2,)

    stock = models.PositiveIntegerField(default=0)

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["id", "slug"]),models.Index(fields=["title"]),models.Index(fields=["created_at"]),]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product_detail",args=[self.id, self.slug])
