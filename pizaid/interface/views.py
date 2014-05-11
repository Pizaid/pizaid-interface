from django.shortcuts import render_to_response
from contents.contents import get_network

# Create your views here.
def index(request):
    return render_to_response('interface/index.html')

def status(request):
    network = get_network()    
    return render_to_response('interface/status.html',
                              {
                                  'ipv4': network.getIPv4()
                              })

def info(request):
    return render_to_response('interface/info.html')

def settings(request):
    return render_to_response('interface/settings.html')
