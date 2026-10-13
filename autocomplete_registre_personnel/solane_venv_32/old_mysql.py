import os
from ctypes import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
os.add_dll_directory(str(BASE_DIR))

mysql = WinDLL(r"libmySQL.dll")

MYSQL = c_void_p
MYSQL_RES = c_void_p
MYSQL_ROW = POINTER(c_char_p)


# mysql_init()
mysql.mysql_init.argtypes = [MYSQL]
mysql.mysql_init.restype = MYSQL


# mysql_real_connect()
mysql.mysql_real_connect.argtypes = [
    MYSQL,      # mysql
    c_char_p,   # host
    c_char_p,   # user
    c_char_p,   # password
    c_char_p,   # database
    c_uint,     # port
    c_char_p,   # unix_socket
    c_ulong     # client_flag
]
mysql.mysql_real_connect.restype = MYSQL


# mysql_close()
mysql.mysql_close.argtypes = [MYSQL]
mysql.mysql_close.restype = None


# mysql_query()
mysql.mysql_query.argtypes = [
    MYSQL,
    c_char_p
]
mysql.mysql_query.restype = c_int


# mysql_error()
mysql.mysql_error.argtypes = [MYSQL]
mysql.mysql_error.restype = c_char_p


# mysql_store_result()
mysql.mysql_store_result.argtypes = [MYSQL]
mysql.mysql_store_result.restype = MYSQL_RES


# mysql_num_rows()
mysql.mysql_num_rows.argtypes = [MYSQL_RES]
mysql.mysql_num_rows.restype = c_ulong


# mysql_num_fields()
mysql.mysql_num_fields.argtypes = [MYSQL_RES]
mysql.mysql_num_fields.restype = c_uint


# mysql_fetch_row()
mysql.mysql_fetch_row.argtypes = [MYSQL_RES]
mysql.mysql_fetch_row.restype = MYSQL_ROW


# mysql_free_result()
mysql.mysql_free_result.argtypes = [MYSQL_RES]
mysql.mysql_free_result.restype = None

conn = mysql.mysql_init(None)

if not mysql.mysql_real_connect(
    conn,
    b"192.168.30.65",
    b"root",
    b"",
    b"BaseSolane",
    3306,
    None,
    0
):
    print(mysql.mysql_error(conn).decode())
    exit()

print("Connexion OK")

def request(request:str):
    ret = mysql.mysql_query(
            conn,
            request.encode("latin1")
        )
    
    if ret != 0:
        print(mysql.mysql_error(conn).decode())
        return None
    else:
        res = mysql.mysql_store_result(conn)
        if res is None:
            return []

        nb = mysql.mysql_num_rows(res)
        cols = mysql.mysql_num_fields(res)
        tableau = []

        for i in range(nb):
            row = mysql.mysql_fetch_row(res)
            
            valeurs = []
            for i in range(cols):
                valeurs.append(row[i].decode("latin1") if row[i] else None)

            tableau.append(valeurs)
        mysql.mysql_free_result(res)
        return tableau

def request_open(file:str):
    path = Path(file)
    if not path.is_absolute():
        path = BASE_DIR / path

    with open(path, "r", encoding="utf-8") as request_file:
        request_string = request_file.read()

    return request(request_string)


def request_replace(file:str, old:list[str], new:list[str]):
    path = Path(file)
    if not path.is_absolute():
        path = BASE_DIR / path

    with open(path, "r", encoding="utf-8") as request_file:
        request_string = request_file.read()

    for i in range(len(old)):
        request_string = request_string.replace(old[i], new[i])

    return request(request_string)