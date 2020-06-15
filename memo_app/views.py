# Create your views here.
"""ビューの目的は一言でいうとHTTPレスポンスを表現するオブジェクトを作成し、返すこと。"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.views.generic import TemplateView
from .forms import PostForm, RecordNumberForm,ChoiceNewOldForm
from .models import *
from django.core.paginator import Paginator

def index_func(aabbb,now_page=1):
    """レコード件数"""
    # if 'record_number' in aabbb.POST:
    #     record_number = aabbb.POST['record_number']
    if 'record_number' in aabbb.session:
        record_number = aabbb.session['record_number'] 
    else:
        record_number = 10
    record_number_form = RecordNumberForm() #forms.pyのRecordNumberFormクラスをインスタンス化 
    record_number_form.initial = {'record_number':str(record_number)}

    """新着順or古い順"""
    if 'new_old' in aabbb.session:
        new_old = aabbb.session['new_old'] 
    else:
        new_old = 'new'
    choice_new_old_form = ChoiceNewOldForm() #forms.pyのChoiceNewOldFormクラスをインスタンス化 
    choice_new_old_form.initial = {'new_old':str(new_old)}


    """Viewでデータベースからデータを取得する"""
    """"モデルクラス.objects.all()
    意味としては、Memoモデルに紐付くオブジェクトを全て取るという意味。
    全てじゃなくて、一部を取ることもできます。
    memos = Memo.objects.filter(取得したい属性=なんとかかんとか) """
    if 'new' in new_old:
        memos = Memo.objects.all().order_by('update_datetime').reverse()
    elif 'old' in new_old:
        memos = Memo.objects.all().order_by('update_datetime')
    # page = Paginator(memos,3)
    page = Paginator(memos,record_number)
    params = {
        'var':'Hello tanaka kouji',
        'page':page.get_page(now_page),
        # 'memos_': memos,
        'form_':PostForm(), #form.pyのclass PostForm(forms.ModelForm):を呼び出している
        'record_number_form_':record_number_form,
        'choice_new_old_form_':choice_new_old_form,
        }
    return render(aabbb,'index_.html',params) #templatesディレクトリ内の"index_.html"ファイル
    """
    Viewはテンプレートと混ぜて使用します。
    render関数でテンプレートとcontext(辞書)と引数request。
    render関数の第3引数として辞書を渡すと、テンプレートに値を渡すことができます。
    今回はparamsという辞書を作成し、そこにキーがvar、バリューがHello worldという形の辞書を作成しました。
    
    次にテンプレートを作成します。 tempaltesというディレクトリとindex_.htmlというファイルを作成してください。

    疑問："aaaaa"という引数をurls.pyで指定していないのになぜあるの？・・・⇒仮引数とのこと？？？
    """

def post_func(bbbb):
    form = PostForm(bbbb.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/') 

    """本来はhtmlをこのviews.pyには書かない"""
def xyz_func(no_meaning):
    return HttpResponse("""
    <html lang="ja">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>koji's xyz</title>
    </head>
    <body>
    <header> koji's xyzのヘッダー</header>
    <nav>
        <a href="/"> 入力画面へ </a><br>
        <a href="/hello"> helloへ </a><br>
        注）本来はこのviews.pyにはhtmlは書かない(templateに書く)。
    </nav>
"""
)


"""表示件数変更機能をwebアプリを閉じるまで持ち回りたい値について、
DBに保存するのではなく、セッションという機能を使う"""
def set_record_number_func(request):
    print("set_record_numberが呼び出され、そのrequest引数",request)
    """set_record_numberメソッドを追加し、セッションに格納。 
    セッションとは一時保管場所みたいなもの。
    追加したメソッドを呼び出すurlをurls.pyに追加。"""
    print("request.session['record_number']",request.session['record_number'])
    print("request.POST['record_number']",request.POST['record_number'])
    request.session['record_number'] = request.POST['record_number']
    """POSTは辞書的なものを呼び出している"""
    return redirect(to='/')

def set_order_option_func(request):
    request.session['new_old'] = request.POST['new_old']
    return redirect(to='/')
    

