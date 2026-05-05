from django.urls import path
from django.contrib import admin
from finance.views import feeCollection, feeDuesReport, feeCollectionReport

urlpatterns = [

    path('feeCo/',feeCollection),
    path('feeDues/', feeDuesReport),
    path('feeColReport/', feeCollectionReport),
]