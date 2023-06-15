from django.urls import path

from . import views

urlpatterns = [path("", views.installment_config, name="installment")]
