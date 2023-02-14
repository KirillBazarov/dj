from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog.feeds import LatestPostsFeedAtom, LatestPostsFeed

sitemaps = {
    "posts": PostSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("xsitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('feed/atom', LatestPostsFeedAtom(), name='latest_posts_feed'),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
