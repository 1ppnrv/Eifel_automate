import fdb
import os
from datetime import datetime, timedelta
import openpyxl

INVALID_CLIENTS = ["PETIT VAL/STMARTIN", "PETIT VAL/VIGNOLS", "LE CAILLOU", "PETIT VAL SCEA", "LES PETITS FRUITS"]
VALID_AUTRES = ["FRAMBOISE", "CASSIS", "MYRTILLE", "MURE", "GROSEILLE", "FRUIT ROUGE MIX"]


con = fdb.connect(
    host="192.168.31.5",
    database="C:\\Ellipson\\Harmony\\Bdd\\Harmony.gdb",
    user="SYSDBA",
    password="PP",
    port=3050,
)

if con:
    path_file = open("path.txt", 'r', encoding="utf-8")
    path = path_file.read()
    path_file.close()
    date = datetime.strptime(datetime.now().strftime(f"%m/%d/%Y"), f"%m/%d/%Y")
    next_date_file = open("next.txt", "r", encoding="utf-8")
    next_date_to_process = next_date_file.read(10)
    next_date_file.close()
    next_date_to_process = datetime.strptime(next_date_to_process, f"%m/%d/%Y")
    
    while next_date_to_process != date:
        file = open("sql_request.sql ", "r")
        request = file.read().replace("date1", next_date_to_process.strftime(f"%m/%d/%Y"))
        cursor = con.cursor()
        cursor.execute(request)
        rows = cursor.fetchall()

        print("date:", next_date_to_process.strftime(f"%m/%d/%Y"))
        poids250 = 0
        poids500 = 0
        autre = 0

        if rows != []:
            for row in rows:
                if not row[0] in INVALID_CLIENTS and not "INDUSTRIE" in row[1]:
                    if "FRAISE" in row[1]:
                        if "G250" in row[2] :
                            if int(row[3]) > 0:
                                print(f"poids250 + {row[3]}")
                                poids250 += int(row[3])
                        elif "G500" in row[2]:
                            if int(row[3]) > 0:
                                print(f"poids500 + {row[3]}")
                                poids500 += int(row[3])
                    else:
                        for fruit in VALID_AUTRES:
                            if fruit in row[2] and not "INDUSTRIE" in row[2] and not "IMPORT" in row[2]:
                                if int(row[3])>0:
                                    print(f"autre + {row[3]}")
                                    autre += int(row[3])
                    


        print(f"Poids 250: {poids250}, poids 500: {poids500}, autre: {autre}")

        excel_file = openpyxl.load_workbook(filename=path, rich_text=True)
        sheet = excel_file[next_date_to_process.strftime(f"%m.%y")]

        # print("E"+str(int(next_date_to_process.strftime(f"%d"))+8))
        sheet["E"+str(int(next_date_to_process.strftime(f"%d"))+8)].value = poids250
        sheet["L"+str(int(next_date_to_process.strftime(f"%d"))+8)].value = poids500
        sheet["S"+str(int(next_date_to_process.strftime(f"%d"))+8)].value = autre
        excel_file.save(filename=path)

        next_date_to_process += timedelta(days=1)

    next_date_file = open("next.txt", "w")
    next_date_file.write(next_date_to_process.strftime(f"%m/%d/%Y"))
else:
    print("no connexion established")