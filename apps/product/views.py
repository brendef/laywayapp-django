from django.shortcuts import render
import json
from django.http import HttpResponse


def product(request):
    if request.method == "GET":
        merchant_id: str = request.GET.get("merchant_id")
        product_id: str = request.GET.get("product_id")
        product_sku: str = request.GET.get("product_sku")
        product_image: str = request.GET.get("product_image")
        product_price: str = request.GET.get("product_price")
        product_name: str = request.GET.get("product_name")
        product_attributes: str = request.GET.get("product_attributes")

        for key, value in json.loads(product_attributes).items():
            product_attributes_dict: dict = {key: [i for i in value.split(",")]}

        context = {
            "merchant_id": merchant_id,
            "product_id": product_id,
            "product_sku": product_sku,
            "product_image": product_image,
            "product_price": product_price,
            "product_attributes": product_attributes_dict,
            "product_name": product_name,
        }

        # todo get data
        # request.session["installment_config"] = {

        # }

        return render(request, "product/product.html", context)

    if request.method == "POST":
        product_config = dict(request.POST.items())

        return HttpResponse("done")
