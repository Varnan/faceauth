# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import base64
import hashlib
import hmac
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
  

from social_django.models import UserSocialAuth

@login_required
def home(request):
    return render(request, 'home.html')



#URL:http://localhost:8000/deauthtication/
@method_decorator(csrf_exempt, name='dispatch')
class DeAuthCallback(View):

    
    def post(self, request, *args, **kwargs):
        try:
            signed_request = request.POST['signed_request']
            encoded_sig, payload = signed_request.split('.')
        except (ValueError, KeyError):
            return HttpResponse(status=400, content='Invalid request')
 
        try:
            decoded_payload = base64.urlsafe_b64decode(payload + "==").decode('utf-8')
            decoded_payload = json.loads(decoded_payload)
 
            if type(decoded_payload) is not dict or 'user_id' not in decoded_payload.keys():
                return HttpResponse(status=400, content='Invalid payload data')
 
        except (ValueError, json.JSONDecodeError):
            return HttpResponse(status=400, content='Could not decode payload')
 
        try:
            secret = settings.SOCIAL_AUTH_FACEBOOK_SECRET
 
            sig = base64.urlsafe_b64decode(encoded_sig + "==")
            expected_sig = hmac.new(bytes(secret, 'utf-8'), bytes(payload, 'utf-8'), hashlib.sha256)
        except:
            return HttpResponse(status=400, content='Could not decode signature')
 
        if not hmac.compare_digest(expected_sig.digest(), sig):
            return HttpResponse(status=400, content='Invalid request')
 
        user_id = decoded_payload['user_id']
 
        try:
            user_account = UserSocialAuth.objects.get(uid=user_id)
        except UserSocialAuth.DoesNotExist:
            return HttpResponse(status=200)
 
        # Mark User as in-active
        if user_account:
            user_account.user.is_active = False
            user_account.user.save()

        return HttpResponse(status=200)