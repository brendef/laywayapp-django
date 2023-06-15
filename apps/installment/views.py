from django.shortcuts import render


def installment_config(request):
    installment_config = request.session["installment_config"]
    context = {}
    return render(
        request=request, template_name="installment/frequency.html", context=context
    )
