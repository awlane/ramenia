from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rameniaapp.models import Noodle, List, Review
from django.contrib.auth.models import User
from rameniaapp.serializers import NoodleSerializer, ListSerializer, ReviewSerializer

@csrf_exempt
def list_rest(request, list_id):
    list = List.objects.get(pk=list_id)

    # get a list
    if request.method == 'GET':
        noodles = list.noodles.all()
        serializer = NoodleSerializer(noodles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # delete a list
    if request.method == 'DELETE':
        if not request.user.is_authenticated or request.user.id != list.user.id:
            return HttpResponse(status=403)
        list.delete()
        return HttpResponse(status=200)

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
        # remove the noodle from the list
        list.noodles.remove(noodle)
        return HttpResponse(status=200)

@csrf_exempt
def user_lists_rest(request, user_id):
    # get all lists for user_id
    lists = List.objects.filter(user__pk=user_id)

    serializer = ListSerializer(lists, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def search_rest(request):
    if request.method == "GET":
        search_type = request.GET.get("type", "noodle")
        search_string = request.GET.get("sstring", None)
        search_tags = request.GET.get("tags", None)
        sort_param = request.GET.get("sortby", "name")
        sort_dir = request.GET.get("sortdir", "asc")
        page = request.GET.get("page", 0)

        # TODO: implement rest of search params

        # filter based on search string
        if search_string:
            noodles = Noodle.objects.filter(name__icontains=search_string)
        else:
            noodles = Noodle.objects.all()

        # filter based on comma separated tags
        if search_tags:
            tags = search_tags.split(',')
            for tag in tags:
                noodles = noodles.filter(tags__name__iexact=tag.strip())

            
        serializer = NoodleSerializer(noodles, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def notifications_rest(request, page):
    # get the user ids following the logged in user
    following = request.user.profile.following.all()
    users = User.objects.filter(profile__in=following)

    # get new reviews
    reviews = Review.objects.filter(reviewer__in=users).order_by('-created')

    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def review_rest(request, review):
    # get the contents of a single review
    review = Review.objects.get(pk=review)
    
    serializer = ReviewSerializer(review)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def reviews_rest(request, noodle):
    # get contents of all reviews for noodle, oreder by date from newest to oldest
    reviews = Review.objects.filter(noodle=noodle).order_by('-created')
    
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse(serializer.data, safe=False)
