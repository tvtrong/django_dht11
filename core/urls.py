
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static

from graphene_django.views import GraphQLView
from graphql_playground.views import GraphQLPlaygroundView
from core.schema import schema
from django.views.decorators.csrf import csrf_exempt  # New library

urlpatterns = [
    path("", include("apps.home.urls")),  # add this
    path("", include("apps.authentication.urls")),  # add this
    path('admin/', admin.site.urls),
    path('api/', csrf_exempt(GraphQLView.as_view(graphiql=False, schema=schema))),
    path('graphql/', csrf_exempt(GraphQLPlaygroundView.as_view(endpoint="http://127.0.0.1:8000/api/"))),
    path("dht11/", include('apps.dht11.urls')),
    path('chats/', include('apps.chats.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
