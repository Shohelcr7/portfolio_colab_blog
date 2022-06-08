from django.urls import path
from . import views


app_name ='login'

urlpatterns = [
path('signup/',views.sign_up , name = 'signup'),
path('login/',views.log_in , name = 'login'),
path('logout/',views.log_out , name = 'logout'),
path('profile/',views.profile , name = 'profile'),
path('update/',views.user_info_update , name = 'update_info'),
path('password/',views.password_change , name = 'password_change'),
path('add-pic/',views.add_profile_pic , name = 'add_profile_pic'),
path('change-pic/',views.change_profile_pic , name = 'change_profile_pic'),

]
