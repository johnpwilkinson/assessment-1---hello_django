
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_view(request):
    context = {'greeting': "Hello World"}
    return render(request, 'index.html', context)