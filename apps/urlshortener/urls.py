from django.urls import path
from apps.urlshortener import views


urlpatterns = [
    path("", views.UrlShorternerView.as_view(), name="url-shortener-api"),
]
