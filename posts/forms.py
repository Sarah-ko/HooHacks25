from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        #fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your post...'}),
            #'image': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'})
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("An image is required for the post.")
        if image.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
            raise forms.ValidationError("Only JPEG, PNG, and GIF images are allowed.")
        return image

