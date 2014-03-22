from django.shortcuts import render

# Create your views here.
def index(request):
    params = {'message': 'hello, world!'}
    return render(request, 'index.html', params)