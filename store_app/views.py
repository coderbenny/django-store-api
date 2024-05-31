from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Client, Item, Sale
from .serializers import ClientSerializer, ItemSerializer, SaleSerializer

# Index route
@api_view(['GET'])
def Index(request):
    return Response({"Home":"Welcome to the store app"}, status=status.HTTP_200_OK)

# All Clients route
@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# All Items route
@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Creating order Route 
@api_view(['POST'])
def create_order(request):
    client_name = request.data.get('client')
    item_id = request.data.get('item_id')

    if not client_name or not item_id:
        return Response({"error": "Client data and item ID are required"}, status=status.HTTP_400_BAD_REQUEST)

    # Handle client creation or retrieval
    client, created = Client.objects.get_or_create(email=client_name['name'], defaults={'name': client_name})

    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    # Create sale
    sale = Sale.objects.create(client=client_name, item=item)

    return Response({"message": "Order created successfully", "sale": SaleSerializer(sale).data}, status=status.HTTP_201_CREATED)

# Total Revenue Route
@api_view(['GET'])
def get_total_revenue(request):
    total_revenue = Sale.objects.aggregate(total_revenue=models.Sum('item__price'))['total_revenue'] or 0
    return Response({"total_revenue": total_revenue}, status=status.HTTP_200_OK)

# Total Sales Route
@api_view(['GET'])
def get_total_sales(request):
    total_sales = Sale.objects.count()
    return Response({"total_sales": total_sales}, status=status.HTTP_200_OK)