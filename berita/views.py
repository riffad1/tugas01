from django.shortcuts import render
from django.http import HttpResponse

from . import views

def index(request):
	 #return HttpResponse("Halaman ini berisi berita terbaru dan rekomendasi berita")
	data = {
	'nav' : [
			['/', 'Home'],
			['/berita', 'Berita'],
			['/kategori', 'Kategori'],
		]
	}
	return render(request, 'home/index.html', data)


def berita(request, judul):
	data = {
	'nama' : judul,
	'nav' : [
			['/', 'Home'],
			['/berita', 'Berita'],
			['/kategori', 'Kategori'],
		]
	}
	return render(request, 'pr/index.html', data)

#def news(request):
	#return HttpResponse("jika ingin berita sesuai kategori masukan jenis kategori di url sesuai keinginan anda!")