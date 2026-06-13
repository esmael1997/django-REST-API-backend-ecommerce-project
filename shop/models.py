from django.db import models
from django.urls import reverse
import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.PROTECT
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True, null=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=12, decimal_places=2)

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["title"]),
            models.Index(fields=["price"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return self.title

    # ----------------------
    # DOMAIN RULES
    # ----------------------
    def is_in_stock(self):
        return self.stock > 0

    def is_available(self):
        return self.is_active and not self.is_deleted and self.stock > 0
    
