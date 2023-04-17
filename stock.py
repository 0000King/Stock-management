
import os
import mysql.connector
import datetime
now = datetime.datetime.now()

def product_mgmt( ):
           while True :
                      print("\t1. Add New Product")
                      print("\t2. List Product")
                      print("\t3. Update Product")
                      print("\t4. Delete Product")
                      print("\t5. Back (Main Menu)")
                      p=int (input("\tEnter Your Choice :"))
                      if p==1:
                                 add_product()
                      if p==2:
                                 search_product()
                      if p==3:
                                 update_product()
                      if p==4:
                                 delete_product()
                      if p== 5 :
                                 break

def purchase_mgmt( ):
           while True :
                      print("\t1. Add Order")
                      print("\t2. List Order")
                      print("\t3. Back (Main Menu)")
                      o=int (input("\tEnter Your Choice :"))
                      if o==1 :
                                 add_order()
                      if o==2 :
                                 list_order()
                      if o== 3 :
                                 break

def sales_mgmt( ):
           while True :
                      print("\t1. Sale Items")
                      print("\t2. List Sales")
                      print("\t3. Back (Main Menu)")
                      s=int (input("\tEnter Your Choice :"))
                      if s== 1 :
                                 sale_product()
                      if s== 2 :
                                 list_sale()
                      if s== 3 :
                                 break

def user_mgmt( ):
           while True :
                      print("\t1. Add user")
                      print("\t2. List user")
                      print("\t3. Back (Main Menu)")
                      u=int (input("\tEnter Your Choice :"))
                      if u==1:
                                 add_user()
                      if u==2:
                                 list_user()
                      if u==3:
                                 break

def create_database():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           print("\tCreating PRODUCT table")
           sql = "CREATE TABLE if not exists product (\
                  pcode int(4) PRIMARY KEY,\
                  pname char(30) NOT NULL,\
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  pcat char(30));"
           mycursor.execute(sql)
           print("\tPRODUCT table created")
           print("\tCreating ORDER table")
           sql = "CREATE TABLE if not exists orders (\
                  orderid int(4)PRIMARY KEY ,\
                  orderdate DATE ,\
                  pcode char(30) NOT NULL , \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  supplier char(50),\
                  pcat char(30));"
           mycursor.execute(sql)
           print("\tORDER table created")
           print("\tCreating SALES table")
           sql = "CREATE TABLE if not exists sales (\
                  salesid int(4) PRIMARY KEY ,\
                  salesdate DATE ,\
                  pcode char(30) references product(pcode), \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  Total double(8,2)\
                  );"
           mycursor.execute(sql)
           print("\tSALES table created")
           print("\tCreating USER table")
           sql = "CREATE TABLE if not exists user (\
                  uid char(6) PRIMARY KEY,\
                  uname char(30) NOT NULL,\
                  upwd char(30));"
           mycursor.execute(sql)
           print("\tUSER table created")

def list_database():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
                   print("\t" , i)

def add_order():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           now = datetime.datetime.now()
           sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values (%s,%s,%s,%s,%s,%s,%s)"
           code=int(input("\tEnter product code :"))
           oid=now.year+now.month+now.day+now.hour+now.minute+now.second
           qty=int(input("\tEnter product quantity : "))
           price=float(input("\tEnter Product unit price: "))
           cat=input("\tEnter product category: ")
           supplier=input("\tEnter Supplier details: ")           
           val=(oid,now,code,price,qty,supplier,cat)
           mycursor.execute(sql,val)
           mydb.commit()

def list_order():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from orders"
           mycursor.execute(sql)
           clrscr()
           print("\tORDER DETAILS")
           print("\t", end="")
           print("-"*85)
           print("\torderid    Date    Product code    price     quantity      Supplier      Category")
           print("\t", end="")
           print("-"*85)
           for i in mycursor:
                      print("\t", i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4],"\t     ",i[5],"\t",i[6])
           print("\t", end="")
           print("-"*85)
                

def db_mgmt( ):
           while True :
                      print("\t1. Database creation")
                      print("\t2. List Database")
                      print("\t3. Back (Main Menu)")
                      p=int (input("\tEnter Your Choice :"))
                      if p==1 :
                                 create_database()
                      if p==2 :
                                 list_database()
                      if p== 3 :
                                 break
def add_product():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
           code=int(input("\tEnter product code :"))
           search="SELECT count(*) FROM product WHERE pcode=%s;"
           val=(code,)
           mycursor.execute(search,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt==0:
                      name=input("\tEnter product name :")
                      qty=int(input("\tEnter product quantity :"))
                      price=float(input("\tEnter product unit price :"))
                      cat=input("\tEnter Product category :")
                      val=(code,name,price,qty,cat)
                      mycursor.execute(sql,val)
                      mydb.commit()
           else:
                      print("\tProduct already exist")
def update_product():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           code=int(input("\tEnter the product code :"))
           qty=int(input("\tEnter the quantity :"))
           sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
           val=(qty,code)
           mycursor.execute(sql,val)
           mydb.commit()
           print("\tProduct details updated")

def delete_product():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           code=int(input("\tEnter the product code :"))
           sql="DELETE FROM product WHERE pcode = %s;"
           val=(code,)
           mycursor.execute(sql,val)
           mydb.commit()
           print("\t", mycursor.rowcount," record(s) deleted");
           
def search_product():
           while True :
                      print("\t1. List all product")
                      print("\t2. List product code wise")
                      print("\t3. List product categoty wise")
                      print("\t4. Back (Main Menu)")
                      s=int (input("\tEnter Your Choice :"))
                      if s==1 :
                                 list_product()
                      if s==2 :
                                  code=int(input("\tEnter product code :"))
                                  list_prcode(code)
                      if s==3 :
                                  cat=input("\tEnter category :")
                                  list_prcat(cat)
                      if s== 4 :
                                 break

def list_product():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from product"
           mycursor.execute(sql)
           print("\tPRODUCT DETAILS")
           print("\t","-"*47)
           print("\tcode    name    price   quantity      category")
           print("\t","-"*47)
           for i in mycursor:
                      print("\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t","-"*47)

def list_prcode(code):
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from product WHERE pcode=%s"
           val=(code,)
           mycursor.execute(sql,val)
           clrscr()
           print("\tPRODUCT DETAILS")
           print("\t","-"*47)
           print("\tcode    name    price   quantity      category")
           print("\t","-"*47)
           for i in mycursor:
                      print("\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t","-"*47)

def sale_product():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           pcode=input("\tEnter product code: ")
           sql="SELECT count(*) from product WHERE pcode=%s;"
           val=(pcode,)
           mycursor.execute(sql,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt !=0 :
                      sql="SELECT * from product WHERE pcode=%s;"
                      val=(pcode,)
                      mycursor.execute(sql,val)
                      for x in mycursor:
                                 print("\t", x)
                                 price=int(x[2])
                                 pqty=int(x[3])
                      qty=int(input("\tEnter no of quantity :"))
                      if qty <= pqty:
                                 total=qty*price;
                                 print ("\tCollect Rs. ", total)
                                 sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                                 val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
                                 mycursor.execute(sql,val)
                                 sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
                                 val=(qty,pcode)
                                 mycursor.execute(sql,val)
                                 mydb.commit()
                      else:
                                 print("\tQuantity not Available")
           else:
                      print("\tProduct is not avalaible")

def list_sale():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * FROM sales"
           mycursor.execute(sql)
           print("\tSALES DETAILS")
           print("\t", "-"*80)
           print("\tSales id  Date    Product Code     Price             Quantity           Total")
           print("\t", "-"*80)
           for x in mycursor:
                      print("\t", x[0],"\t",x[1],"\t",x[2],"\t   ",x[3],"\t\t",x[4],"\t\t",x[5])
           print("\t", "-"*80)
                              
def list_prcat(cat):
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           print (cat)
           sql="SELECT * from product WHERE pcat =%s"
           val=(cat,)
           mycursor.execute(sql,val)
           print("\tPRODUCT DETAILS")
           print("\t","-"*47)
           print("\tcode    name    price   quantity      category")
           print("\t","-"*47)
           for i in mycursor:
                      print("\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t","-"*47)

def add_user():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           uid=input("\tEnter emaid id :")
           name=input("\tEnter Name :")
           paswd=input("\tEnter Password :")
           sql="INSERT INTO user values (%s,%s,%s);"
           val=(uid,name,paswd)
           mycursor.execute(sql,val)
           mydb.commit()
           print("\t", mycursor.rowcount, " user created")

def list_user():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT uid,uname from user"
           mycursor.execute(sql)
           print("\tUSER DETAILS")
           print("\t","-"*27)
           print("\tUID\t\tname")
           print("\t","-"*27)
           for i in mycursor:
                      print("\t",i[0],"\t",i[1])
           print("\t","-"*27)

while True:
           print("\tSTOCK MANAGEMENT")
           print("\t****************\n")
           print("\t1. PRODUCT MANAGEMENT")
           print("\t2. PURCHASE MANAGEMENT")
           print("\t3. SALES MANAGEMENT")
           print("\t4. USER MANAGEMENT")
           print("\t5. DATABASE SETUP")
           print("\t6. EXIT\n")
           n=int(input("\tEnter your choice :"))
           if n== 1:
                      product_mgmt()
           if n== 2:
                      os.system('cls')
                      purchase_mgmt()
           if n== 3:
                      sales_mgmt()
           if n== 4:
                      user_mgmt()
           if n==5 :
                      db_mgmt()
           if n== 6:
                      break