"""policefc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from apps.posts.views import (index, blog, post,
                              search, add_post_tiny,
                              edit_post_tiny, post_update,
                              post_delete, post_create)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('createpost/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    # allauth path
    path('accounts/', include('allauth.urls')),

    # apis endpoints
    path('dev/', include('apps.players.urls')),
    path('dev/', include('frontend.urls')),
    path('add/post_tiny', add_post_tiny, name='add_post_tiny'),
    path('edit/post_tiny/<int:post_tiny_id>/',
         edit_post_tiny, name='edit_post_tiny'),

]
# Added this content
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
