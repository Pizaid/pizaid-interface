from django.shortcuts import render_to_response
from dbusinterface.pizaidnetwork import PizaidNetwork

# Create your views here.
def index(request):
    return render_to_response('interface/index.html')

def status(request):
    network = PizaidNetwork()
    properties = network.get_properties()
    return render_to_response('interface/status.html',
                              {
                                  'ipv4': properties.Get_ipv4()
                              })

def info(request):
    return render_to_response('interface/info.html')

def settings(request):
    return render_to_response('interface/settings.html')
