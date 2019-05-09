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

from apps.soccerplayers.views import(player_list,executive_team_list,
                                    technical_team_list,technical_member_detail,
                                    create_player,player,
                                    update_player, delete_player,
                                    executive, create_executive)


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

    ## roles lists
    path('players/', player_list, name='player-list'),
    path('executives/', executive_team_list, name='executive-list'),
    path('technical-teams/', technical_team_list, name='technical-member-list'),



    path('players/<id>/', player, name='player-detail'),
    path('executives/<id>/', executive, name='executive-detail'),
    path('technical-teams/<id>/', post, name='technical-member-detail'),
    path('createplayer/', create_player, name='create-player'),
    path('createexecutive/', create_executive, name='create-executive'),
    path('players/<id>/update/', update_player, name='update-player'),
    path('players/<id>/delete/', delete_player, name='delete-player'),
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
