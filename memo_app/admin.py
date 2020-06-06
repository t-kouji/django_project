from django.contrib import admin
from .models import Memo

# Register your models here.
"""↓の一行を追加するだけで管理者画面からメモアプリが使えるようになる。これはdjangoの元々の機能"""
admin.site.register(Memo)
