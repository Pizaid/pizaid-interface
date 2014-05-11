from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('interface/index.html')

def status(request):
    return render_to_response('interface/status.html')

def info(request):
    return render_to_response('interface/info.html')

def settings(request):
    return render_to_response('interface/settings.html')
