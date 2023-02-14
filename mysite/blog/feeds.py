from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from blog.models import Post

class LatestPostsFeedAtom(Feed):
    title = "My Blog"
    link = "/blog/"
    description = "Latest posts from my blog"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])

    def item_pubdate(self, item):
        return item.created_on

    def feed_extra_kwargs(self, obj):
        if isinstance(self.feed_type, Rss201rev2Feed):
            return {'xml_lang': 'en'}
        elif isinstance(self.feed_type, Atom1Feed):
            return {'language': 'en'}
        return {}


class LatestPostsFeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)