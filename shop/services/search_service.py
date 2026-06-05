from django.db.models import Q, Case, When, IntegerField, Value
from shop.models import Product

def search_products(queryset, query):
    if not query:
        return queryset
    
    return queryset.annotate(
        search_score=Case(
            When(title__icontains=query, then=Value(3)),
            When(description__icontains=query, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )
    ).filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ).order_by("-search_score")
    