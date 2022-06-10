from django.urls import path
from . import views

urlpatterns=[


    path('',views.index,name="indexView"),
    # path('contact/',views.contact,name="contact"),
    path('privacy/',views.privacy,name="privacy"),

]