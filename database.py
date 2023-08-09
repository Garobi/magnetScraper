import pymysql

# database connection
connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="", database="magnet")
cursor = connection.cursor()

def insereMedia(url, idwebsite, title):
    sql = f"INSERT INTO media (url, idwebsite, title, country) VALUES ( '{url}', {idwebsite}, '{title}', 'BR' ) "
    cursor.execute(sql)
    print(cursor.fetchall())
    connection.commit()

def finalizaConexao():
    cursor.close()
    connection.close()
# url = "https://lapumia.org/os-tres-mosqueteiros-dartagnan-torrent-2023-dublado-download/"
# title = "Os Três Mosqueteiros: D’Artagnan Torrent (2023) Dual Áudio WEB-DL 1080p FULL HD Download"