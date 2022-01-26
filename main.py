import requests
from mysql import connector
import json

db = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'db_akademik_0502'
)

baseURL = 'https://api.abcfdab.cfd/'

def fetch_data():
    endpoint = 'students'
    r = requests.get(baseURL + endpoint)
    output = r.json()
    output_data = output['data']
    for i in output_data:
       data = (i['nim'], i['nama'], i['jk'], i['jurusan'], i['alamat'])  
       sql = 'INSERT INTO `nama` (no, nim, nama, jk, jurusan, alamat) VALUES ( NULL, %s, %s, %s, %s, %s)'
       db_i = db.cursor()
       db_i.execute(sql, data)
       db.commit()

def show_all():
    query = 'SELECT * FROM nama'
    db_i = db.cursor()
    db_i.execute(query)
    output = db_i.fetchall()
    for i in output:
        print(i)

def limit_data():
    pass

def limit_nim():
    pass

def options():
    print ('1. Show All Data')
    print ('2. Show Limit Data')
    print ('3. Show Limit NIM')

def main():
    options()
    p = int(input('Pilih Options : '))
    if p == 1:
        show_all()
    if p == 2:
        limit_data()
    if p == 3:
        limit_nim()

if __name__ == '__main__':
    main()    

    