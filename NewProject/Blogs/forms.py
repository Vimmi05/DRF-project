from django.forms import ModelForm
from Blogs.models import BlogModel

class BlogForm(ModelForm):
    class Meta:
        model = BlogModel
        fields = "__all__"

