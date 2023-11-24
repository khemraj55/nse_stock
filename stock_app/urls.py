from .views import *
from django.urls import path

urlpatterns=[
    path('live-stock-data/<str:symbol>/', LiveStockDataView.as_view(), name='live_stock_data'),
    path('extract-stock-data/', ExtractStockDataView.as_view(), name='extract_stock_data'),    
]