from django.db import models
from datetime import datetime


class Upload(models.Model):
    downloadDocount = models.IntegerField(default=0, verbose_name="浏览次数")
    code = models.CharField(max_length=8, verbose_name='code')
    dateTime = models.DateTimeField(default=datetime.now())
    path = models.CharField(max_length=32, verbose_name='路径')
    name = models.CharField(max_length=32, verbose_name='文件名')
    fileSize = models.CharField(max_length=10, verbose_name='大小')
    PCIP = models.CharField(max_length=32, verbose_name='地址', default='')

    class Meta():
        verbose_name = 'download'
        db_table = 'download'

    def __str__(self):
        return self.name

