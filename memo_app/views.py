from django.shortcuts import render ,redirect
from django.views.generic import TemplateView

from .models import *

def index_func(aiueo):
    memos = Memo.objects.all()
    params = {
        'var':'Hello tanaka kouji',
        'memos_': memos
    }
    return render(aiueo,'index_.html',params) #templatesディレクトリ内の"index_.html"ファイル
    """
    Viewはテンプレートと混ぜて使用します。
    まずはHello Worldを表示させます。
    render関数でテンプレートとcontextを混ぜる(aiueo)もといった感じです。
    render関数の第3引数として辞書を渡すと、テンプレートに値を渡すことができます。
    今回はparamsという辞書を作成し、そこにキーがvar、バリューがHello worldという形の辞書を作成しました。
    次にテンプレートを作成します。 tempaltesというディレクトリとindex_.htmlというファイルを作成してください。

    疑問："aiueo"という引数をurls.pyで指定していないのになぜあるの？・・・⇒仮引数とのこと？？？
    """

# Create your views here.
