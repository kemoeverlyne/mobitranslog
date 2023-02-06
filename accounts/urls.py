from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import signup, login_view, forgot_password, landing

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('', landing, name="landing")
]
urlpatterns += staticfiles_urlpatterns()
