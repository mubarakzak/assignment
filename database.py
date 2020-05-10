import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
conn.commit()


cursor.execute('''CREATE TABLE wed
         (AccountNO INT PRIMARY KEY     NOT NULL,
         firstNAME           TEXT    NOT NULL,
         lastNAME            TEXT     NOT NULL,
         date of birth        INT,
         Password         INT);''')
cursor.close()

import sqlite3 as my_database

class Create:
    def func_CreateData(self):

        # Get the sql connection
        conn =my_database.sqlite.getConnection()
        AccountNo= input('Enter AccNo = ')       
        firstName = input('Enter firstName = ')
        lastName= input('Enter lastName = ')
        DOB= input('Enter date of birth  = ')
        password= input('Enter password = ')

        try:
           query = "Insert Into Customer(AccountNo,firstName,lastName,date of birth,password Values(?,?)" 
           cursor = conn.cursor()

           # Execute the sql query
           cursor.execute(query, [AccountNo,firstName,lastName,DOB,password])

           # Commit the data
           conn.commit()
           print('Data Saved Successfully')

        except:
             print('Something wrong, please check')

        finally:
           # Close the connection
           conn.close()

import sqlite3 as my_database

class Read:
    def func_ReadData(self):   
        # Get the sql connection
        conn =my_database.sqlite.getConnection()
        cursor = conn.cursor()

        # Execute the sql query
        cursor.execute('Select * from wesilyes')

        # Print the data
        for row in cursor:
            print('row = %r' % (row,))

import sqlite3 as my_database ;

class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        conn = my_database.sqlite.getConnection() 

        AccountNo = input('Enter Customer AccNO = ')
    
        try:
           # Fetch the data which needs to be updated
           sql = "Select * From Customer Where AccountNo = ?" 
           cursor = conn.cursor()
           cursor.execute(sql, [AccountNo])
           item = cursor.fetchone()
           print('Data Fetched for AccountNo = ', AccountNo)
           print('AccountNo\t\t firstName\t\t\t lastName\t\t\t DOB\t\t\t password')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2], item[3], item[4]))
           print('-------------------------------------------')
           print('Enter New Data To Update Customer Record ')

        
           AccountNo= input('Enter AccNo = ')       
           firstName = input('Enter firstName = ')
           lastName= input('Enter lastName = ')
           DOB= input('Enter date of birth  = ')
           password= input('Enter password = ')
           query = "Update Customer Set AccountNo = ?, firstName = ?, lastName =?, DOB =?, Where password = ?" 
       
           # Execute the update query
           cursor.execute(query, [AccountNo, firstName, lastName, DOB, password])
           conn.commit()
           print('Data Updated Successfully')

        except:
             print('Something wrong, please check')

        finally:
           # Close the connection
           conn.close()

import sqlite3 as my_database;

class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        conn = my_database.sqlite.getConnection()

        AccountNo= input('Enter Customer AccountNo = ')
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From Customer Where AccountNo = ?" 
           cursor = conn.cursor()
           cursor.execute(sql, [AccountNo])
           item = cursor.fetchone()
           print('Data Fetched for AccountNo = ', AccountNo)
           print('AccountNo\t\t firstName\t\t\t lastName\t\t\t DOB\t\t\t password')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2], item[3], item[4]))
           print('-------------------------------------------')
           confirm = input('Are you sure to delete this record (Yes/No)?')

           # Delete after confirmation
           if confirm == 'Yes':
               deleteQuery = "Delete From Customer Where AccountNo = ?"
               cursor.execute(deleteQuery,[AccountNo])
               conn.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            conn.close()

