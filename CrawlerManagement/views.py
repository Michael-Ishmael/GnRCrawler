from django.shortcuts import render

# Create your views here.


def index(request):
    companies = ['123', '456', '789']
    context = {'companies': companies};
    return render(request, 'index.html', context)
