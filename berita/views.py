from django.shortcuts import render
from django.http import HttpResponse

from . import views

def index(request):
	 return HttpResponse("Ini adalah halaman home")

def berita(request, judul):
	data = {'nama' : judul}
	return render(request, 'pr/index.html', data)

#def news(request):
	#return HttpResponse("ini halaman berita")