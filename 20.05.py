"""employee project"""


class DataBase:
    import sqlite3
    def __init__(self,db_name):
        self.db_name = db_name
        self.connection = None
    def connect(self):
        self.connection = self.sqlite3.connect(self.db_name+'.db')
    def cursor(self):
        if self.connection is not None:
            return self.connection.cursor()
class Table(DataBase):
    def __init__(self,db_name,table_name,id,full_name,email,address,salary,pose):
        super().__init__(db_name)
        self.table_name = table_name
        self.id = id
        self.full_name = full_name
        self.email = email
        self.address = address
        self.salary = salary
        self.pose = pose
    def create_table(self):
        command = f"""CREATE TABLE {self.table_name} (
        {self.id} int PRIMARY KEY,
        {self.full_name} varchar(30) NOT NULL,
        {self.email} varchar(30) UNIQUE ,
        {self.address} varchar(20),
        {self.salary} int DEFAULT(50000),
        {self.pose} varchar(15) NOT NULL
        );"""
        cursor = self.cursor()
        cursor.execute(command)
class Person:
    def __init__(self,table_obj,id,full_name,email,address,salary,position):
        self.table = table_obj
        self.id = id
        self.full_name = full_name
        self.email = email
        self.address = address
        self.salary = salary
        self.position = position
    def insert_table(self):
        print(table.connection)
        command = f"""INSERT INTO {table.table_name} (
        {table.id}, {table.full_name}, {table.email},{table.address},{table.salary}, {table.pose}) 
        VALUES({self.id},'{self.full_name}','{self.email}','{self.address}',{self.salary},'{self.position}');"""
        cursor = table.cursor()
        try:
            cursor.execute(command)
        except table.sqlite3.IntegrityError as e:
            print(e)
        table.connection.commit()

    def select(self, mode=None, value1 = None, value2 = None):
        if mode is None:
            command = f"""SELECT * FROM {table.table_name};"""
        elif mode == 'between' and value1 and value2:
            command = f"""SELECT * FROM {table.table_name} WHERE {table.salary} BETWEEN {value1} AND {value2};"""
        cursor = table.cursor()
        cursor.execute(command)
        print(cursor.fetchall())
        table.connection.commit()
    def update(self, column, new_value):
        command = f"""UPDATE {table.table_name} SET {column} = {new_value} WHERE {table.id} == {self.id}"""
        cursor = table.cursor()
        cursor.execute(command)
        table.connection.commit()

table = Table('employee','employee','id','full_name','email','address','salary','position')
table.connect()

# table.create_table()
vova = Person(table,1,'zinko17','zinko17@mail.ru','lalaland',50001,'developer')
# vova.insert_table()
# vova.select()
aliya = Person(table,2,'aliya','aliya@gmail.com','lalaland',100001,'developer')
aliya.insert_table()
# aliya.update('salary',-1)
aliya.select(mode='between', value1='-2', value2='1000')
# aliya.select()
