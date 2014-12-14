from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from CrawlerManagement.models import Company
from .forms import UploadFileForm
from django.core.urlresolvers import reverse
from business.data import CsvLoader

# Create your views here.
import csv


def index(request):
    companies = Company.objects.order_by('-Name')[:5]
    form = UploadFileForm()
    context = {'companies': companies, 'uploadForm': form}
    return render(request, 'index.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
            except Exception as ex:
                return render_to_response('index.html', {'form': form, 'exception': ex.message})
            else:
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UploadFileForm()
    return render_to_response('index.html', {'form': form})


def handle_uploaded_file(f):
    loader = CsvLoader()
    loader.handle_uploaded_file(f)
