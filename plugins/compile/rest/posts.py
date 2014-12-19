from docutils import nodes
from docutils.parsers.rst import Directive, directives

try:
    import micawber
except ImportError:
    micawber = None  # NOQA


from nikola.plugin_categories import RestExtension


class Plugin(RestExtension):

    name = "rest_posts"

    def set_site(self, site):
        self.site = site
        Posts.site = site
        directives.register_directive('posts', Posts)
        return super(Plugin, self).set_site(site)


class Posts(Directive):
    """ Restructured text extension for inserting a list of posts."""
    has_content = False
    required_arguments = 1
    optional_arguments = 999

    def run(self):
        all_posts = sorted(self.site.timeline, key=lambda post: post.date, reverse=True)

        tags = frozenset(self.arguments)
        tag_posts = [post for post in all_posts if tags & set(post.alltags)]
        for post in tag_posts:
            post.compile('en')
        ctx = {}
        ctx["template_name"] = 'posts_list.tmpl'
        ctx.update(self.site.GLOBAL_CONTEXT)
        ctx['posts'] = tag_posts
        ctx['lang'] = 'en'

        data = self.site.template_system.render_template('posts_list.tmpl', None, ctx)
        contents = data

        return [nodes.raw('', contents, format='html')]
