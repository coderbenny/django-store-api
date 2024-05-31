from django.urls import path

from  . import views

app_name = 'store_app'
urlpatterns = [
    path("", views.Index, name="Index"),
    path('order/', views.create_order, name='create_order'),
    path('total_revenue/', views.get_total_revenue, name='total_revenue'),
    path('total_sales/', views.get_total_sales, name='total_sales'),
]