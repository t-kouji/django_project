"""
Djangoにはモデルのためのフォームを作成するModelFormというクラスが用意されています。
これを利用することで、スムーズにレコードの保存を行うことができます。
 forms.pyというファイルをアプリフォルダに新規作成します。
"""

from django import forms
from .models import Memo

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }