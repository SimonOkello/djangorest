from rest_framework import generics
from . models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.


class SnippetList(generics.ListCreateAPIView):
    """
    Generic view to list and create snippet instance
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view to list and create snippet instance
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
