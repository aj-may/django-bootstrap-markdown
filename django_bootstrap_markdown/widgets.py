from django.forms import Textarea
from django.template import Context
from django.template.loader import get_template


class MarkdownInput(Textarea):
    def __init__(self, attrs=None, image_control=True):
        self.image_control = image_control

        default_attrs = {
            'class': 'form-control',
        }
        if attrs:
            default_attrs.update(attrs)

        super(Textarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        textarea = Textarea.render(self, name, value)

        t = get_template('django_bootstrap_markdown/widget.html')
        c = Context({
            'show_image_button': self.image_control,
            'textarea': textarea,
        })

        return t.render(c)

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/marked/0.2.9/marked.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/ekko-lightbox/3.0.3a/ekko-lightbox.min.js',
            'js/jquery.textarea.min.js',
            'js/django_bootstrap_markdown.js',
        )
        css = {
            'all': (
                '//cdnjs.cloudflare.com/ajax/libs/ekko-lightbox/3.0.3a/ekko-lightbox.min.css',
                'css/django_bootstrap_markdown.css',
            )
        }
