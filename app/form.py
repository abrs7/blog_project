from django import forms

from app.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
class Comment(forms.ModelForm):


    class Meta():
        model = Comment
        fields = ('author', 'text', '')        
