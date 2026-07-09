import psycopg2

def table():
    conn =psycopg2.connect(dbname="postgres",user ="postgres",password="Password",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''create table employee(name text,id int,age int)''')

    print("Table created Successfully")

    conn.commit()
    conn.close()

def data():
    conn =psycopg2.connect(dbname="postgres",user ="postgres",password="Amanjain1008@",host="localhost",port="5432")

    cursor = conn.cursor()

    name =input('enter name:')
    id=input('Enter id')
    age=input('enter age')

    query ='''insert into employee(name,id,age) values (%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    
    # cursor.execute('''insert into employee(name,id,age)values('Aman',01,21);''')

    print("Data Added Successfully")

    conn.commit()
    conn.close()    

data()

# def extract():
#     conn =psycopg2.connect(dbname="postgres",user ="postgres",password="Amanjain1008@",host="localhost",port="5432")

#     cursor = conn.cursor()
#     cursor.execute('''Select * from employees;''')
#     print(cursor.fetchone())

#     # print("Data Added Successfully")

#     conn.commit()
#     conn.close()    

# data()

 
