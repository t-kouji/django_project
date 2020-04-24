"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))


インターネット上のすべてのページには、独自のURLが必要です。 
それによって、アプリケーションが、URLを元にアクセスしてきたユーザに、みせるべきサイトを表示します。
Djangoでは URLconf（URL設定）と呼ばれるものを使います。
URLconfはパターンの集まりで、適切なviewを見つけるために、
DjangoがリクエストされたURLと照合するものです。
"""
from django.contrib import admin
from django.urls import path ,include
"""
基本的にdjango_app/urls.pyは簡潔なままにしておきます。
その為、memo_app/urls.pyの内容を
django_app/urls.pyの方でincludeを使い参照しています。
'memo_app.urls'はmemo_appディレクトリ内のurls.pyという意味だと思う。
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('memo_app.urls'))
]
