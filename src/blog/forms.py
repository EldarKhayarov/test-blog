from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Заголовок', required=True)
    text = forms.CharField(label='Текст', required=True, widget=forms.Textarea)
