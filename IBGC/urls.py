from django.urls import path
from .views import upload_image,upload_and_resize,home, dashboard, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('upload_image/', upload_image, name='upload_image'),
    path('upload/', upload_and_resize, name='upload'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),

]
