from django.urls import path #djangoの標準モジュール
from . import views #(from . )同ディレクトリ内のviews.pyをimport

urlpatterns = [
    path('',views.index_func,name='index_aaa'),
    path('post', views.post, name='post_aaa'),
    path('<int:now_page>', views.index_func, name='indeb_aa'),
]#views.pyのdef index_funcを召喚。name = って何??
#urlにname='index_aaa'のように名前を設定しておくと設定しているurlが変更になっても該当箇所は全部書き換えなくて済むとのこと。

from django.urls import path
from . import views
