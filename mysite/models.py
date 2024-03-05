from django.db import models

# Create your models here.
#建立一個Post的類別, (到時在資料庫中會有一個對應的資料表)
#model主要負責要存取的資料模型, 以pythony class類別形式來定義,後端Django自動會把這個類別中的設定對應到資料庫系統
#把資料取出則是view.py中處理
#取得的資料用美觀有彈性的方式輸出就是用templates
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    #設定用於指定此紀錄的一些相關設定, 其中ordering是用來設定當紀錄被取得時回傳的順序
    class Meta:
        ordering=('-pub_date',)
    #如果要顯示出來就以文章標題title這個欄位的內容做為顯示代表
    def __str__(self):
        return self.title