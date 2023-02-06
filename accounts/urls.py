from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import signup, login_view, forgot_password

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
]
urlpatterns += staticfiles_urlpatterns()
