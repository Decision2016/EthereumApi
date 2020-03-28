from django.conf.urls import url, include
from request.views import Request

urlpatterns = [
    url(r'^api/', include('blockGet.urls')),
    url(r'^request/',Request.as_view())
]

