from django.forms import Textarea
from django.utils.safestring import mark_safe

class MarkdownInput(Textarea):
    def render(self, name, value, attrs=None):
        try:
            self.attrs['class'] = 'form-control %s' % self.attrs['class']
        except KeyError:
            self.attrs['class'] = 'form-control'

        try:
            self.attrs['style'] = 'height: 400px; resize: none; %s' % self.attrs['style']
        except KeyError:
            self.attrs['style'] = 'height: 400px; resize: none;'

        textarea = Textarea.render(self, name, value)

        markup = """
        <div class="row md-edit">
            <div class="col-sm-6">
                <div class="pull-right">
                    <button type="button" class="btn btn-sm btn-default"><span class="glyphicon glyphicon-picture"></span> Add Image</button>
                </div>
                <h5 class="text-muted">Markdown</h5>
                %s
            </div>
            <div class="col-sm-6 hidden-xs">
                <h5 class="text-muted">Preview</h5>
                <div class="form-control preview" style="height: 400px; overflow: auto;"></div>
            </div>
        </div>
        """ % textarea

        return mark_safe( markup )

    class Media:
        js = (
            '//cdnjs.cloudflare.com/ajax/libs/marked/0.2.9/marked.min.js',
            'js/django_bootstrap_markdown_editor.js',
        )