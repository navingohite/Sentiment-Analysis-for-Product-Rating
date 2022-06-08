from glob import escape
from django.shortcuts import render

from .models import Product, Review
from .ratings import rating_analysis


def index(request):
    products = [product for product in Product.objects.all()]

    if request.method == 'POST':
        review_all = ""
        product_id = int(request.POST["product_id"])
        reviews = Review.objects.filter(product_id=product_id)
        for review in reviews:
            review_all = review_all + " " + review.review
        
        review_count = len(reviews)
        selected_product = Product.objects.filter(id=product_id)[0]
        stars, half_stars = rating_analysis(review_all)
    else:
        reviews = Review.objects.all()
        selected_product =products[0]
        stars, half_stars = 0, 0
        review_count = 0

    if stars > 3:
        rating = "Good"
    elif stars < 2:
        rating = "Poor"
    else:
        rating = "Average"

    context = {
        "products": products,
        "selected_product": selected_product,
        "stars": list(range(stars)),
        "half_stars": list(range(half_stars)),
        "rating": rating,
        "count": review_count,
    }

    print(context)
    print("ID", selected_product.id)
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html", {})