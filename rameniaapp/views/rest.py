from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rameniaapp.models import Noodle, List
from rameniaapp.serializers import NoodleSerializer

@csrf_exempt
def list_rest(request, list_id):
    if request.method == 'GET':
        list = List.objects.get(pk=list_id)
        noodles = list.noodles.all()
        serializer = NoodleSerializer(noodles, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def list_mod_rest(request, list_id, noodle_id):
    list = List.objects.get(pk=list_id)
    
    # check auth
    if not request.user.is_authenticated or request.user.id != list.user.id:
        return HttpResponse(status=403)
    
    noodle = Noodle.objects.get(pk=noodle_id)
    if request.method == 'PUT':
        # add the noodle to the list
        list.noodles.add(noodle)
        return HttpResponse(status=200)
    elif request.method == 'DELETE':
        # add the noodle to the list
        list.noodles.remove(noodle)
        return HttpResponse(status=200)
