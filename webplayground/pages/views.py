from django.urls import reverse, reverse_lazy
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
class pageListView(ListView):
   model = Page
   queryset = Page.objects.all().order_by('-id')

class pageDetailView(DetailView):
    model = Page
    
class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')