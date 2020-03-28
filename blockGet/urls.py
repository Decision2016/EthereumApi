from django.conf.urls import url
from blockGet import views

urlpatterns = [
    url(r'^blockinfo', views.GetBlockInfo.as_view()),
]