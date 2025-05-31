from django.urls import path
from . import views
from .views import pageListView, pageDetailView, PageCreate



pages_patterns = ([
    path('', pageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', pageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
], 'pages')