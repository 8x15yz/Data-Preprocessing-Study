import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threePlusFive.settings')
django.setup()

from tpf.models import CopUBr, BR
list05 = BR.objects.all()

with open('./LPOINT_BIG_COMP_03_COP_U.csv') as csv03:
    csv03 = csv.reader(csv03)
    zon_hlv = ''
    zon_mcls = ''
    next(csv03, None)
    # cnt = 0
    for row03 in csv03:
        for arr in list05:
            if arr.br_c == row03[12]:
                zon_hlv = arr.zon_hlv
                zon_mcls = arr.zon_mcls
                print(row03[12], zon_hlv, zon_mcls)
                CopUBr.objects.create(
                    cust = row03[0],
                    rct_no = row03[1],
                    cop_c = row03[2],
                    chnl_dv = row03[3],
                    de_dt_y = row03[4],
                    de_dt_m = row03[5],
                    de_dt_d = row03[6],
                    vst_dt_y = row03[7],
                    vst_dt_m = row03[8],
                    vst_dt_d = row03[9],
                    de_hr = row03[10],
                    buy_am = row03[11],
                    br_c = row03[12],
                    zon_hlv = zon_hlv,
                    zon_mcls = zon_mcls
                )
                # cnt += 1
                break
        # if cnt == 100:
        #     break