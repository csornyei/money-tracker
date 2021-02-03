from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from tracker.models import Spending
from tracker.serializers import SpendingSerializer

class SpendingList(APIView):
    def get(self, request, format=None):
        currency_filter = request.GET.get('currency', False)
        if currency_filter:
            spendings = Spending.objects.all().filter(currency=currency_filter)
        else:
            spendings = Spending.objects.all()
        order_param = request.GET.get('order', False)
        if order_param:
            spendings = spendings.order_by(order_param)
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
