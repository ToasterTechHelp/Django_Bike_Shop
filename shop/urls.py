from django.urls import path
from . import views
from .views import BikeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bikes/', views.bikes, name='bikes_list'),
    path('bikes/<int:pk>/', BikeView.as_view(), name='bike_detail'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
