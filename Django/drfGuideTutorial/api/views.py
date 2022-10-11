from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Item
from api.serializer import itemSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    """
        Fetch Datas From Item Table.
        
        Args:
            request: <request object>
        
        Returns:
            Response.
    """
    items = Item.objects.all()
    serializedItem = itemSerializer(items,many=True)
    return Response(serializedItem.data)

@api_view(['POST'])
def addData(request):
    serializer = itemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteData(request,id):
    Item.objects.get(id=id).delete()
    response = {'response':'itemDeleted'}
    return Response(response)

@api_view(['PUT'])
def updateData(request,id):
    item = Item.objects.get(id=id)
    serializer = itemSerializer(instance=item,data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



    