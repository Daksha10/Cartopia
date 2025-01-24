import mysql.connector
cnx=mysql.connector.connect(user='root',password='ManoDaksha@123',host='127.0.0.1',database='Cartopia')
cursor=cnx.cursor()
query= "SELECT * FROM Cartopia.Products"
cursor.execute(query)
for (id,name,uom_id,price_per_unit) in cursor:
    print(id,name,uom_id,price_per_unit)
cnx.close()