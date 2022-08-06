"""
Core views for app.
"""
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return render(request, 'app/index.html')


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return Response({'healthy': True})
