from django.shortcuts import render
from appAlert import FCMManager
from django.http.response import HttpResponse
from pyfcm import FCMNotification
from fcm_django.models import FCMDevice
from django.conf import settings

# Create your views here.
def sendNotifications(request):
    if request.method == 'GET':
        title = "this is title"
        desc = "this is description"
       
        # image = notification_image.objects.all()
        # # all token
        # tokens = user_push_token.objects.all()
        # all token array
        #alltokens = ['eqo1b1RoTSiGBJ-anw90HW:APA91bEW-IFaaj9PrC2nTd0g7Kc5J3mrxPfP72LM4V_V09lZQ_g0uYVuQ0TU--NDrrrkhOI6OG6VoNW1M6DvgBeMeCldR2kMOrMNWawlZ2WddGy9zVFRyQbBr1Mj_K2nfK0wYbQzujzF']
        # image
        alltokens = []
        push_img = {}
        tokens = FCMDevice.objects.all()
        print(tokens)
        for tokenlist in tokens:
            alltokens.append(tokenlist.registration_id)
        print(alltokens)
        # if image:
        #     push_img = {'image': image[0].image.url}
        FCMManager.sendPush(title, desc, alltokens, push_img)
        
        return HttpResponse(request,'yes')
    
def send_push(request):
    title = "this is title"
    desc = "this is description"
    data_message = {
                "title": title,
                "body": desc,
            }
    push_service = FCMNotification(api_key=settings.FCM_API_KEY)
    try:
        tokens = 'eqo1b1RoTSiGBJ-anw90HW:APA91bEW-IFaaj9PrC2nTd0g7Kc5J3mrxPfP72LM4V_V09lZQ_g0uYVuQ0TU--NDrrrkhOI6OG6VoNW1M6DvgBeMeCldR2kMOrMNWawlZ2WddGy9zVFRyQbBr1Mj_K2nfK0wYbQzujzF'
        registration_ids = [tokens]
        result = push_service.multiple_devices_data_message(registration_ids=registration_ids,
                                                                data_message=data_message)
        #FCMManager.test_send()
        print(result)
        return HttpResponse(request,'yes')
    except Exception as e:
        print(e)
        return HttpResponse(request,'yes')
