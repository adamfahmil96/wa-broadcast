from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'Judul': 'Kirim Pesan'
    }
    return render(request, 'pesan/index.html', context)