from django.shortcuts import render
from django.http import HttpResponse

from . import views

def index(request):
	return HttpResponse('<h1>Selamat Datang di Home</h1>')

def berita(request):
	return HttpResponse('<h1>Silahkan Masukan Kategori Via URL</h1>')

def kategori(request, judul):
	return HttpResponse("Ini adalah kategori berita %s." % judul)	