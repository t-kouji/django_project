"""入力フォームを作るためのファイルforms.py"""

from django import forms
from .models import Memo

"""Djangoにはモデルのためのフォームを作成するModelFormというクラスが用意されています。
これを利用することで、スムーズにレコードの保存を行うことができます。
 forms.pyというファイルをアプリフォルダに新規作成します。
メモを登録する際には、モデルに紐づく入力フォームとしてModelFormを使用する。"""
class PostForm(forms.ModelForm):
    """forms.ModelFormクラスではMetaクラスのクラス変数（model）でモデルと紐づけ、その後は
    フォームコンポーネントで使うフィールドをクラス変数（fields）に設定するだけで済む。"""
    class Meta:
        model = Memo #クラス変数（model）でモデルと紐づけ（ここではmodels.pyのclass Memo）
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }


"""
forms.Formを使用
ChoiceFieldはプルダウンやラジオボタン用
choicesに(値, 画面表示名)のタプルを設定すると画面表示される
"""
CHOICE_FIELD_RECODE_NUMBERS = (
    ('5', '5件'),
    ('10', '10件'),
    ('15', '15件'),
    ('20', '20件'),
    ('25', '25件'),
    ('30', '30件'),
)
class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), 
        choices=CHOICE_FIELD_RECODE_NUMBERS,
    )
    print("forms.pyのclass RecordNumberForm(forms.Form):のrecord_number",record_number)


CHOICE_NEW_OLD = (
    ('new', '新着順'),
    ('old', '古い順'),
)
class ChoiceNewOldForm(forms.Form):
    hogehoge = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}), 
        choices=CHOICE_NEW_OLD ,
    )
