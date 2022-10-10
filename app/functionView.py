from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Create': '/product-create/',
        'Update':'/update-product/<str:pk>/',
        'Delete':'/delete-product/<str:pk>/',
        'ProductView':'/product-detail/<str:pk>/',
        'List':'/products/'
    }
    return Response(api_urls)

@api_view(['GET'])
def getProducts(request):
    prods = Product.objects.all()
    serialized_data = ProductSerializer(prods,many=True)
    # data = model_to_dict(prods,fields=['name','price']) 
    return Response(serialized_data.data)



@api_view(['GET','POST'])
def postProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response({'invalid':"The posted product's is format is incorrect"},status=400)


@api_view(['GET'])
def getProductDetail(request,pk):
    prod = Product.objects.all().filter(id=pk).first()
    serializer = ProductSerializer(instance=prod,many=False)

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request,pk):
    if not pk.isnumeric():
        return Response("Product id must be numeric value")
    prod = Product.objects.all().filter(id=pk).first()
    serializer = ProductSerializer(instance=prod,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    if not pk.isnumeric():
        return Response("Product id must be numeric value")
    prod = Product.objects.all().filter(id=pk).first()
    if prod:
        prod.delete()
        return Response("Product has been deleted successfully")
    
    return Response("Product doesn't Exit")