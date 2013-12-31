from django.forms import Textarea
from django.utils.safestring import mark_safe

class MarkdownInput(Textarea):
    def __init__(self, attrs=None, image_control=True):
        self.image_control = image_control

        default_attrs = {
            'class': 'form-control',
            'style': 'height: 400px; resize: none;',
        }
        if attrs:
            default_attrs.update(attrs)

        super(Textarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        textarea = Textarea.render(self, name, value)

        if self.image_control:
            image_control_markup = """
            <div class="pull-right">
                <button type="button" class="btn btn-sm btn-default markdown-image-btn"><span class="glyphicon glyphicon-picture"></span> Add Image</button>
            </div>
            """
        else:
            image_control_markup = ""

        markup = """
        <div class="row md-edit">
            <div class="col-sm-6">
                %s
                <h5 class="text-muted">Markdown</h5>
                %s
            </div>
            <div class="col-sm-6 hidden-xs">
                <h5 class="text-muted">Preview</h5>
                <div class="form-control preview" style="height: 400px; overflow: auto;"></div>
            </div>
        </div>
        """ % (image_control_markup, textarea)

        return mark_safe( markup )

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/marked/0.2.9/marked.min.js',
            'js/jquery.textarea.min.js',
            'js/django_bootstrap_markdown_editor.js',
        )