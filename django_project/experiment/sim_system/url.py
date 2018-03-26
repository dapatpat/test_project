from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^stusys$', views.index),
    url(r'selection$',views.selection),
    url(r'addInfos$',views.addInfos),
    url(r'^showall$',views.showall),
]