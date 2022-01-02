from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.
from userProfile.models import UserProfile
from userProfile.serializers import UserProfileSerializer

@csrf_exempt
def profileApi(request,id=0):
    if request.method =='GET':
        profiles = UserProfile.objects.all()
        profiles_serializer = UserProfileSerializer(profiles,many=True)
        return JsonResponse(profiles_serializer.data, safe=False)
    elif request.method == 'POST':
        profiles_data = JSONParser().parse(request)
        profiles_serializer = UserProfileSerializer(data=profiles_data)
        if(profiles_serializer.is_valid):
            profiles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        profile_data = JSONParser().parse(request)
        profileFound = UserProfile.objects.get(token =profile_data['token'])
        profiles_serializer = UserProfileSerializer(profileFound, data=profile_data)
        if (profiles_serializer.is_valid):
            profiles_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        profiles = UserProfile.objects.get(token=id)
        profiles.delete()
        return JsonResponse("Deleted Successfully", safe=False)
