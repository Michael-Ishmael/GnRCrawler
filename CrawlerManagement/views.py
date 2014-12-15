from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from CrawlerManagement.models import Company
from .forms import UploadFileForm
from django.core.urlresolvers import reverse
from business.data import CsvLoader
from business.web import WebsiteLocator

# Create your views here.
import csv


def index(request):
    companies = Company.objects.order_by('-Name')[:50]
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


def find_company_website(request, company_ref):
    locator = WebsiteLocator()
    try:
        company_url_response = locator.find_website(company_ref)
        return JsonResponse(company_url_response)
    except Exception as ex:
        return JsonResponse({"success": False, "message":ex.message})