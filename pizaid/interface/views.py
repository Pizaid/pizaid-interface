from django.shortcuts import render_to_response
from dbusinterface.pizaidnetwork import PizaidNetwork
from dbusinterface.pizaidstorage import PizaidStorage
from dbusinterface.pizaidpower import PizaidPower

# Create your views here.
def index(request):
    return render_to_response('interface/index.html')

def status(request):
    network = PizaidNetwork().get_properties()
    storage = PizaidStorage().get_properties()
    power   = PizaidPower().get_properties()

    names = storage.Get_names()
    return render_to_response('interface/status.html',
                              {
                                  'ipv4' : network.Get_ipv4(),
                                  'names': names,
                                  'total': storage.Get_capacity_kb(names[0]),
                                  'used' : storage.Get_usage_kb(names[0]),
                                  'usage': storage.Get_usage_percent(names[0]),
                                  'ac'   : power.Is_ac_plugin()
                              })

def info(request):
    return render_to_response('interface/info.html')

def settings(request):
    return render_to_response('interface/settings.html')
