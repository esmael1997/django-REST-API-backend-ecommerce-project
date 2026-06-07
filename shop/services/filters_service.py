def filter_products_by_price(queryset, min_price=None, max_price=None):

    if min_price is not None:
        queryset = queryset.filter(price__gte=min_price)

    if max_price is not None:
        queryset = queryset.filter(price__lte=max_price)

    return queryset