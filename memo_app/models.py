from django.db import models

# Create your models here.

class Memo(models.Model):
    content = models.CharField(max_length=2000)
    update_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        下記は"http://127.0.0.1:8001/admin/memo_app/memo/"の画面に反映される。
        """
        return 'id:' + str(self.id) + ',更新日時' 
        + str(self.update_datetime)
