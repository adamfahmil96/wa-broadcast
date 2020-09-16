from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Judul': 'Lihat Kontak'
    }
    return render(request, 'kontak/index.html', context)