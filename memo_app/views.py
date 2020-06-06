# Create your views here.

from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from .forms import PostForm
from .models import *
from django.core.paginator import Paginator

def index_func(aaaaa,now_page=1):
    memos = Memo.objects.all()
    page = Paginator(memos,3)
    params = {
        'var':'Hello tanaka kouji',
        'page':page.get_page(now_page),
        # 'memos_': memos,
        'form_':PostForm()
        }
    return render(aaaaa,'index_.html',params) #templatesディレクトリ内の"index_.html"ファイル
    """
    Viewはテンプレートと混ぜて使用します。
    まずはHello Worldを表示させます。
    render関数でテンプレートとcontextを混ぜる(aaaaa)もといった感じです。
    render関数の第3引数として辞書を渡すと、テンプレートに値を渡すことができます。
    今回はparamsという辞書を作成し、そこにキーがvar、バリューがHello worldという形の辞書を作成しました。
    次にテンプレートを作成します。 tempaltesというディレクトリとindex_.htmlというファイルを作成してください。

    疑問："aaaaa"という引数をurls.pyで指定していないのになぜあるの？・・・⇒仮引数とのこと？？？
    """

def post(bbbb):
    form = PostForm(bbbb.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/')