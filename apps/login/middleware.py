from social_django.middleware import SocialAuthExceptionMiddleware
from social_core import exceptions as social_exceptions
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect

# Crear un middleware y detectar cualquier excepción, lista de excepciones: 
# https://github.com/omab/python-social-auth/blob/master/social/exceptions.py

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, 'AuthCanceled'):
            return redirect('login')
        else:
            raise exception