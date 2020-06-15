from django.urls import path #djangoの標準モジュール
from . import views #(from . )同ディレクトリ内のviews.pyをimport
from django.http import HttpResponse #本来はurl.pyには入れないが勉強の為に（ビギ本P29）。

def hello_func(aiueo):
    return HttpResponse("hello django!")
    """ この関数がいわゆるビュー。
    ビューはHTTPレスポンスを表現するオブジェクトを作成し、返す。
    つまり上のHttpResponse()の引数にどんな文字列を渡すかを考えればよい。
    ちなみにビューの引数(ここでいう(aiueo))にはHTTPリクエストを表現したオブジェクトが渡されている。
    これはつまり、ユーザーから送信されたデータやリクエストメソッドなどの情報が詰まっていて、
    処理によってはそれらのデータを利用しHTTPレスポンスを作成することができる。

    本来はviews.pyにまとめておくが別にurl.pyにも書けるぞという勉強の為（ビギ本P40）。"""

urlpatterns = [
    path('hello/',hello_func), #このファイルurl.pyの関数hello_aaを呼ぶ（ビギ本P29）。本来はviews.pyの該当関数を呼ぶ。
    path('xyz/',views.xyz_func),
    path('post', views.post_func, name='post_aaa'),
    path('<int:now_page>', views.index_func, name='no_meaning'),
    path('s_r_n', views.set_record_number_func, name='set_record_number_n'),
    path('s_o_o',views.set_order_option_func,name='set_order_option_n'),
    path('',views.index_func,name='index_aaa'),
]#views.pyのdef index_funcを召喚。name = って何??
#urlにname='index_aaa'のように名前を設定しておくと設定しているurlが変更になっても該当箇所は全部書き換えなくて済むとのこと。

