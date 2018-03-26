from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^get/$', views.get),
    url(r'^get/get1.html',views.get1),
    url(r'^get/get2.html',views.get2)
}
