from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^post$',views.post),
    url(r'^post/post1$',views.post1),
    url(r'cook',views.cook),
    url(r'^post/se$',views.se),
    url(r'^post/session1$',views.session1),
    url(r'^post/session2$',views.session2),
    url(r'^post/logout$',views.logout),
    url(r'^liuyanban$',views.handle),
    url(r'^finish$',views.liuyanban),
    url(r"^area$",views.area),
]