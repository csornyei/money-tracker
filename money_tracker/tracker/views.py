from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from tracker.models import Spending
from tracker.serializers import SpendingSerializer

class SpendingList(APIView):
    def get(self, request, format=None):
        print(request)
        spendings = Spending.objects.all()
        serializer = SpendingSerializer(spendings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpendingDetail(APIView):
    def get_object(self, id):
        try:
            return Spending.objects.get(pk=id)
        except Spending.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        spending = self.get_object(id)
        serializer = SpendingSerializer(spending)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        spending = self.get_object(id)
        serializer = SpendingSerializer(spending, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        spending = self.get_object(id)
        spending.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
