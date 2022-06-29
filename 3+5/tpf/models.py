from django.db import models

# Create your models here.
class Trade(models.Model):
    cust = models.IntegerField()
    rct_no = models.IntegerField()
    cop_c = models.IntegerField()
    chnl_dv = models.IntegerField()
    de_dt = models.IntegerField()
    vst_dt = models.IntegerField()
    de_hr = models.IntegerField()
    buy_am = models.IntegerField()
    br_c = models.IntegerField()
    cop_c = models.IntegerField()
    zon_hlv = models.IntegerField()
    zon_mcls = models.IntegerField()