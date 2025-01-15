from django.urls import path, include
from oauth2_provider import urls as oauth2_urls


urlpatterns = [
	path('auth/', include(oauth2_urls)),
]