from django.shortcuts import render, HttpResponse
from apps.merchant.models import Merchant, FrequencySettings


def installment_config(request):
    product = request.session.get("product")
    merchant = Merchant.objects.filter(id=product["merchant_id"]).values()
    frequencies = FrequencySettings.objects.filter(id__in=(1, 2)).values()

    context = {"merchant": merchant, "frequencies": frequencies}

    return render(
        request=request, template_name="installment/installment.html", context=context
    )
