import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'threePlusFive.settings')
django.setup()

from tpf.models import BR

with open('./LPOINT_BIG_COMP_05_BR.csv') as csv05:
    csv05 = csv.reader(csv05)
    next(csv05, None)
    for row05 in csv05:
        print(row05)
        BR.objects.create(
            br_c = row05[0],
            zon_hlv = row05[2],
            zon_mcls = row05[3]
        )