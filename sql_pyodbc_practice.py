import pyodbc
# i = int(raw_input('Provide a min price: '))

cnxn = pyodbc.connect('DSN=KubrickSQLServer')
cursor = cnxn.cursor()
# cursor.execute("""select productnumber, name , standardcost from production.product
#                where standardcost > ?""", i)
# row = cursor.fetchall()
# top10 = row[:10]
# for r in top10:
#     print r
#
# j = float(raw_input('Please provide a price increase: '))
# cursor.execute("""
# update production.product set standardcost=standardcost*? from production.product
# """,j)
# cnxn.commit()
i = str(raw_input('Please provide a Product Name: '))
j = int(raw_input('Please provide a Quantity: '))
k = float(raw_input('Please provide a Cost: '))
cursor.execute("""
insert into sales.mysales
(productname, qty, cost)
Values (?,?,?),
""", i, j, k)
cnxn.commit()
print 'total rows inserted : {}'.format(cursor.rowcount)
