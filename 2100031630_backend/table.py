import mysql.connector

import queries

con=mysql.connector.connect(host='localhost',port='3306',database='saifer',user='root',password='root')

if con.is_connected:
    try:
        cur=con.cursor()

        #CUSTOMER TABLE
        cur.execute('create table if not exists Customers(CustomerID int primary key, FirstName varchar(20), LastName varchar(20), Email varchar(50), DateOfBirth Date)')
        
        #PRODUCTS TABLE
        cur.execute('create table if not exists Products(ProductID int primary key, ProductName varchar(20), Price int)')

        #ORDERS TABLE
        cur.execute('create table if not exists Orders(OrderID int primary key, CustomerID int, OrderDate Date)')


        #ORDERITEMS TABLE
        cur.execute('create table if not exists OrderItems(OrderItemID int primary key, OrderID int, ProductID int, Quantity int)')


        #INSERTION
        i1='insert into customers values(%s,%s,%s,%s,%s)'
        v1=[(1,'John','Doe','john.doe@example.com','1985-01-15'),(2,'Jane','Smith','jane.smith@example.com','1990-06-20')]
        cur.executemany(i1,v1)

        i2='insert into Products values(%s,%s,%s)'
        v2=[(1,'Laptop',1000),(2,'Smartphone',600),(3,'Headphones',100)]
        cur.executemany(i2,v2)

        i3='insert into Orders values(%s,%s,%s)'
        v3=[(1,1,'2023-01-10'),(2,2,'2023-01-12')]
        cur.executemany(i3,v3)

        i4='insert into OrderItems values(%s,%s,%s,%s)'
        v4=[(1,1,1,1),(2,1,3,2),(3,2,2,1),(4,2,3,1)]
        cur.executemany(i4,v4)

        con.commit()


        #QUERIES
        queries.Query.querfun(con)
        

    except Exception as e:
        print(e)
