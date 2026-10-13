from old_mysql import *
import sys
from datetime import datetime
from pathlib import Path
import json
import openpyxl

debug = False
BASE_DIR = Path(__file__).resolve().parent

app_data_file = open(BASE_DIR / "app.json", "r", encoding="utf-8")
app_data = json.load(app_data_file)
app_data_file.close()
last_matrs_dates = app_data["last_matrs_dates"]
matrs = last_matrs_dates["matrs"]
dates = last_matrs_dates["dates"]
path = app_data["path"]

valid_soc = ["GEAC", "GEEL", "CAILLOU", "PETIT FR", "PETIT VA"]

nb_val = 0

for i in range(len(dates) - 1, -1, -1):
    if datetime.strptime(dates[i], r"%Y%m%d") < datetime.now():
        dates.pop(i)
        matrs.pop(i)
#print(app_data)


def req_infos(matr):
    infos_req = request_replace("request_infos.sql", ["matr1"], [matr])
    if not infos_req:
        return None
    
    return infos_req[0]

news_contr = request_replace("request_contrats.sql", ["datenow"], [datetime.strftime(datetime.now(), r"%Y-%m-%d")])
if news_contr is None:
    print("request not ok")
    sys.exit()

if not news_contr:
    print("No new contracts found")
    sys.exit()


for line in news_contr:
    print(line)

    type_contr = line[0]
    matr = line[1]
    if matr in matrs:
        continue

    curr_dates_result = request_replace("request_dates.sql", ['matr1'], [matr])
    if not curr_dates_result or not curr_dates_result[0] or len(curr_dates_result[0]) < 2:
        print("dates not ok")
        continue

    curr_dates = curr_dates_result[0][1] if curr_dates_result[0][1] != "22220101" else curr_dates_result[0][0]
    if not curr_dates:
        print("dates not ok")
        continue

    curr_dates = curr_dates[0:8]

    formatted_date = datetime.strftime(datetime.strptime(curr_dates,r"%Y%m%d"), r"%Y-%m-%d")

    infos = req_infos(matr)

    print(infos)
    print(curr_dates)
    print(type_contr)
    if not line[2] in valid_soc:
        continue

    for i in range(len(infos)):
        if infos[i] == None:
            infos[i] = ""

    curr_path = path+app_data["folders"][line[2]]
    if not debug:
        cases = 1
        excel_file = openpyxl.load_workbook(filename=curr_path, rich_text=True)
        sheet = excel_file.active
        while sheet["A"+str(cases)].value != None:
            cases += 1
        # print(cases)
        sheet["A"+str(cases)].value = infos[1]
        sheet["B"+str(cases)].value = infos[0]
        sheet["C"+str(cases)].value = infos[9]
        sheet["D"+str(cases)].value = "FEMININ" if infos[8] == 'F' else "MASCULIN"
        sheet["E"+str(cases)].value = datetime.strftime(datetime.strptime(infos[6],r"%Y-%m-%d"), r"%d/%m/%Y")
        sheet["F"+str(cases)].value = infos[7]
        sheet["G"+str(cases)].value = infos[2]+" "+infos[3]+" "+infos[4]+" "+infos[5]
        sheet["H"+str(cases)].value = "OUVRIER SAISONNIER AGRICOLE"
        sheet["I"+str(cases)].value = datetime.strftime(datetime.strptime(curr_dates,r"%Y%m%d"), r"%d/%m/%Y")
        sheet["K"+str(cases)].value = "X" if type_contr != "300" else ""
        sheet["L"+str(cases)].value = "X" if type_contr == "300" else ""
        excel_file.save(filename=curr_path)
    else:
        print(curr_path)

    nb_val += 1
    matrs.append(matr)
    dates.append(curr_dates)

print(app_data)
print(nb_val)
if debug:
    sys.exit()

with open(BASE_DIR / "app.json", "w", encoding="utf-8") as file:
    json.dump(app_data, file, ensure_ascii=False, indent=4)