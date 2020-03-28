from django.db import models

# Create your models here.


class BlockInfo(models.Model):
    BlockId = models.BigIntegerField()
    BlockHash = models.TextField()
    TimeStamp = models.BigIntegerField()