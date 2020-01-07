from django.urls import path
from snippets import views

# Write your urls here

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippets'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet_detail'),
]
