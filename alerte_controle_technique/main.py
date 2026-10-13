import tkinter as tk
from time import sleep
import openpyxl
from pathlib import Path
import json
from datetime import datetime,timedelta

root = tk.Tk()
root.withdraw()  # Cache la fenêtre principale

rappel = tk.BooleanVar()

def open_window(text):
    win = tk.Toplevel()
    win.title("Contrôle technique")
    tk.Label(win, text=text).pack(padx=20, pady=40)
    tk.Checkbutton(win, text="Ne plus me le rapeller", variable=rappel).pack(anchor='w')
    tk.Button(win, text="Fermer", command=win.destroy).pack(pady=10)
    root.wait_window(win)
    if rappel.get():
        seen["dates"][index] = date.strftime(r"%d/%m/%Y")


# sleep(7)

BASE_DIR = Path(__file__).resolve().parent

seen_file = open(BASE_DIR / "seen.json", "r", encoding="utf-8")
seen = json.load(seen_file)
seen_file.close()

excel = openpyxl.load_workbook("P:\\SERVICE_ADMINISTRATIF\\VEHICULES\\ETAT PARC 2026\\Etat parc 2026.xlsx")
sheet = excel["TRAVAUX"]

while True:
    i = 3
    
    while sheet["A"+str(i)].value != None:
        if type(sheet["I"+str(i)].value) == str:
            try:
                date = datetime.strptime(sheet["I"+str(i)].value, r"%d/%m/%Y").date()
            except:
                date = datetime.now() - timedelta(weeks=5000)
                date = date.date()
        elif type(sheet["I"+str(i)].value) == datetime:
            date = sheet["I"+str(i)].value.date()

        if sheet["A"+str(i)].value in seen["seen"]:
            index = seen["seen"].index(sheet["A"+str(i)].value)

            if seen["dates"][index]:
                if datetime.strptime(seen["dates"][index], r"%d/%m/%Y").date() != date:
                    if date > datetime.now().date() and date - timedelta(days=17) < datetime.now().date():
                        open_window(f"Contrôle technique de {sheet["B"+str(i)].value}, immatriculation {sheet["A"+str(i)].value} prévu le {date.strftime("%d/%m/%Y")}")

            else:
                if date > datetime.now().date() and date - timedelta(days=17) < datetime.now().date():
                    open_window(f"Contrôle technique de {sheet["B"+str(i)].value}, immatriculation {sheet["A"+str(i)].value} prévu le {date.strftime("%d/%m/%Y")}")
                    
        else:
            seen["seen"].append(sheet["A"+str(i)].value)
            seen["dates"].append(None)

        i += 1
    with open(BASE_DIR / "seen.json", "w", encoding="utf-8") as file:
        json.dump(seen, file, ensure_ascii=False, indent=4)
    sleep(3600)



