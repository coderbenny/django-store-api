from django.urls import path

from  . import views

app_name = 'store_app'
urlpatterns = [
    path("", views.Index, name="Index"), # Index Route
    path("clients/", views.get_clients, name="Clients"), # All Clients Route
    path("items/", views.get_items, name="Items"), # All Items Route
    path("sales/", views.all_sales, name="sales"), # All Sales Route
    path('order/', views.create_order, name='create_order'), # Route for Creating an Order
    path('total-revenue/', views.get_total_revenue, name='total_revenue'), # Total Revenue Route
    path('total-sales/', views.get_total_sales, name='total_sales'), # Total Sales Route
    path('items/view/<int:item_id>/', views.view_item, name='view_item'), # Item By ID Route
    path('items/<int:item_id>/', views.delete_item, name='delete_item'), # Route for Deleting Item
]