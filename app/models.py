import psycopg2


class CreateTables:
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.dbconnect.autocommit = True
        self.cursor = self.dbconnect.cursor()
    

     
    def create_user_table(self):
        user_table_create = "CREATE TABLE Users(User_Id serial PRIMARY KEY, FirstName varchar(100) NOT NULL, LastName varchar(100) NOT NULL,Email varchar(100) NOT NULL, password varchar(100) NOT NULL)"
        self.cursor.execute(user_table_create)

   
class Users():
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.dbconnect.autocommit = True
        self.cursor = self.dbconnect.cursor()

    def create_new_user(self,Fname,Lname,Email,Password):
        new_user =   "INSERT INTO Users(FirstName, LastName, Email, password) VALUES(%s,%s,%s,%s)",(Fname, Lname, Email,Password)
        self.cursor.execute(new_user)

    

class Requests():
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.dbconnect.autocommit = True
        self.cursor = self.dbconnect.cursor()

    def create_request_table(self):
        request_table_create = "CREATE TABLE Requests(Request_Id serial PRIMARY KEY, UserId INT REFERENCES Users(User_Id), RequestType varchar(100) NOT NULL, RequestDetails varchar(200) NOT NULL )"
        self.cursor.execute(request_table_create)
    
    
if __name__ == '__main__':
    User_table = CreateTables()
    Request_table = Requests() 

    

 

    
