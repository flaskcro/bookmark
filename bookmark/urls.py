from django.conf.urls import url

from bookmarks.views import *
import os.path

site_media = os.path.join(
    os.path.dirname(__file__),'site_media'
)

urlpatterns = [
    # Examples:
     url(r'^$|^home$', 'bookmarks.views.home'),
     url(r'^home2$', 'bookmarks.views.home2'),
     url(r'^user/(\w+)/$', 'bookmarks.views.user_page'),
     url(r'^login/$','django.contrib.auth.views.login'),
     url(r'^logout/$','logout_page'),
     url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'docuement_root':site_media}),
    # url(r'^blog/', include('blog.urls')),
]
