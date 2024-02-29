# middleware.py

from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectIfLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # If the user is logged in and tries to access the login page,
            # redirect them to the home page
            if request.path == reverse('login-page'):
                return HttpResponseRedirect(reverse('home-page'))

        response = self.get_response(request)
        return response
