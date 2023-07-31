# # In middleware.py
# from django.shortcuts import redirect
# from django.urls import reverse
#
#
# class RedirectLoggedInUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.user.is_authenticated:
#
#             return redirect(reverse('index'))
#
#         response = self.get_response(request)
#         return response
