from django.shortcuts import render

def pagina_navidena(request):
    return render(request, 'index.html')  # ← Sin 'navidad/'