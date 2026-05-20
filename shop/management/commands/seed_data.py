import random
from faker import Faker
from django.core.management.base import BaseCommand
from shop.models import Category, Product

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake products"
    
    def handle(self, *args, **kwargs):
        category = ["Mobile", "Laptop", "Monitor","keyborad", "Mouse",]
        category_objects = []
        for category_name in category:
            category, created = Category.objects.get_or_create(
                slug=category_name.lower(),
                defaults={
                "name": category_name,
                }
            )
            category_objects.append(category)
        for _ in range(60):
            
            title = fake.sentence(nb_words=3)

        Product.objects.create(
            category=random.choice(category_objects),
            title=title,
            slug=f"{title.lower().replace(' ', '-')}-{random.randint(1000,9999)}",
            description=fake.text(),
            price=random.randint(100, 10000),
            stock=random.randint(1, 200),
            available=True,
        )

        self.stdout.write(
            self.style.SUCCESS("Fake data generated successfully!")
)