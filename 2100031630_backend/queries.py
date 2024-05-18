class Query:
    def querfun(con):
        cur=con.cursor()


        #Q1. List all customers.
        cur.execute('select FirstName,LastName from customers')
        res=cur.fetchall()
        for record in res:
            print('FIRST NAME: ',record[0],',', 'LAST NAME: ',record[1])
            print()
        
        #Q2. Find all orders placed in January 2023.
        cur.execute('select  * from Orders where MONTH(OrderDate)=1 and YEAR(OrderDate)=2023')
        res2=cur.fetchall()
        for r in res2:
            print('Order id:',r[0],',','Customer id:',r[1],',','OrderDate:',r[2])
            print()

        
        #Q3. Get the details of each order, including the customer name and email.
        cur.execute('select oi.orderID, oi.productID, p.productName, c.FirstName, c.LastName, c.email from OrderItems oi\
                     join Products p on oi.productID=p.ProductID join Orders o on oi.OrderID=o.OrderID\
                     JOIN Customers c on o.CustomerID=c.CustomerID order by c.CustomerID asc')
        res3=cur.fetchall()
        for r in res3:
            print('OrderID: ',r[0],',','ProductID: ',r[1],',','ProductName: ',r[2],',','User Name: ',r[3]+' '+r[4],',','User Email',r[5])
            print()

        
        #Q4. List the products purchased in a specific order (e.g., OrderID = 1).
        cur.execute('select oi.productID, p.productName, oi.quantity, p.price from OrderItems oi join Products p on oi.productid=p.productid')
        res4=cur.fetchall()
        for r in res4:
            print('ProductID: ',r[0],',','Product Name: ',r[1],',','Quantity: ',r[2],',','Price: ',r[3])
            print()

        #Q5. Calculate the total amount spent by each customer
        cur.execute('select c.FirstName,c.LastName, sum(p.price*oi.Quantity) from orderitems oi\
                     join products p on oi.productid=p.productid\
                     join orders o on oi.orderid=o.orderid join customers c on o.customerid=c.customerid group by oi.orderid')
        res5=cur.fetchall()

        for r in res5:
            print('Name of the customer: ',r[0]+' '+r[1],',','Total Amount Spent: ',r[2])
            print()

        
        #Q6. Find the most popular product (the one that has been ordered the most).
        cur.execute('select oi.productid, p.productname, sum(oi.quantity) as quan from orderitems oi\
                    join products p on oi.productid=p.productid group by oi.productid order by quan desc limit 1')
        res6=cur.fetchall()
        for r in res6:
            print('Product Name: ',r[1],',','Quantity: ',r[2])
            print()

        #Q7. Get the total number of orders and the total sales amount for each month in 2023.
        cur.execute('select year(o.orderdate) as year, month(o.orderdate) as month, count(distinct o.orderid), sum(p.price * oi.quantity) from orders o\
                     join orderitems oi on o.orderid = oi.orderid join products p on oi.productid = p.productid\
                     where year(o.orderdate) = 2023 group by year(o.orderdate), month(o.orderdate) order by year, month')
        res7=cur.fetchall()
        for r in res7:
            print('Year: ',r[0],',','Month: ',r[1],',','Numer of orders: ',r[2],',','Total amount in the month: ',r[3])
            print()

        #Q8.Find customers who have spent more than $1000.
        cur.execute('select c.Firstname, c.LastName, oi.orderid, sum(oi.quantity*p.price) as pr  from customers c\
                     join orders o on c.customerid=o.customerid join orderitems oi on oi.orderid=o.orderid\
                     join products p on p.productid=oi.productid group by oi.orderid having pr>1000')
        res8=cur.fetchall()
        for r in res8:
            print('Name: ',r[0]+' '+r[1],',', 'Amount Spent: ',r[3])
            print()