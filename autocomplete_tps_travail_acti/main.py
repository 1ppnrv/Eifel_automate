from old_mysql import *
from datetime import datetime,timedelta
from pathlib import Path
from time import sleep
import openpyxl

BASE_DIR = Path(__file__).resolve().parent

mois = {
    "01":"C",
    "02":"D",
    "03":"E",
    "04":"F",
    "05":"G",
    "06":"H",
    "07":"I",
    "08":"J",
    "09":"K",
    "10":"L",
    "11":"M",
    "12":"N"
}

debug = True
path = "Z:\\ADV\\\\Christophe\\STATS 2026\\HEURES ACTIVITES.xlsx"
requests = ["request_actis_global.sql", "request_actis_serre.sql", "request_actis_recolte.sql", "request_actis_condi.sql"]
request_time = ["request_time0.sql", "request_time1.sql", "request_time2.sql", "request_time3.sql"]

while debug:
    excel = openpyxl.load_workbook(filename=path)
    sheet = excel[datetime.strftime(datetime.now(), "%Y")]

    date1 = datetime.strftime(datetime.now() - timedelta(weeks=2), "%Y%m")+"01"
    date2 = date1[:6]+"31"
    for i in range(4):
        actis = request_replace(requests[i],["date1", "date2"], [date1, date2])
        for acti in actis:
            curr_acti = acti[1]
            hours = request_replace(request_time[i], ["date1", "date2", "act1"], [date1, date2, str(curr_acti)])[0][3]
            hours = int(float(hours))
            print(curr_acti,hours)
            count = 1
            while sheet["A"+str(count)].value != curr_acti and count < 100:
                count += 1
            if count != 100:
                sheet[mois[date2[4:6]]+str(count)].value = hours
    excel.save(filename=path)


    # debug = False
    sleep(36000)
