from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Property
from .utils import get_all_properties
from .serializers import PropertySerializer

@method_decorator(cache_page(60*15), name='dispatch')
class PropertyListView(APIView):
    def get(self, request):
        queryset = get_all_properties()
        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)
