import pyodbc
import csv
cnxn = pyodbc.connect('DSN=KubrickSQLServer')
cursor = cnxn.cursor()
# i = str(raw_input('Please provide a file directory: '))


with open('C:\Users\Student22\Desktop\usedcars.csv', "r") as usedcars:
    Uc = csv.DictReader(usedcars, delimiter=',', skipinitialspace='True')
    for c in Uc:
        km = int(c['km'])
        year = int(c['year'])
        powerPS = int(c['powerPS'])
        avgPrice = float(c['avgPrice'])

        if int(c['powerPS']) > 200:
            cursor.execute("""
            insert into
            [Adventureworks2012].sales.carsales
            (km, year, powerPS, avgPrice)
            Values (?,?,?,?)
            """, km, year, powerPS, avgPrice)
            cnxn.commit()








# cursor.execute("""
# bulk insert
# [Adventureworks2012].sales.mysales
# from 'i'
# with(
# fieldterminator=',',
# keepidentity
# )
# """, i)
# cnxn.commit()
