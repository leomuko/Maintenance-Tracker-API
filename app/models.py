import psycopg2


class USERS:
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.cursor = self.dbconnect.cursor()
    

     
    def create_user_table(self):
        user_table_create = "CREATE TABLE Users(User_Id serial PRIMARY KEY, FirstName varchar(100) NOT NULL, LastName varchar(100) NOT NULL,Email varchar(100) NOT NULL, password varchar(100) NOT NULL)"
        self.cursor.execute(user_table_create)
        self.dbconnect.commit()

    def create_new_user(self,Fname,Lname,Email,Password):
        new_user =   "INSERT INTO Users(FirstName, LastName, Email, password) VALUES('{}','{}','{}','{}')".format(Fname, Lname, Email,Password)
        
        self.cursor.execute(new_user)
        self.dbconnect.commit()

    def login_user(self,email,password):
        user = "SELECT * FROM Users WHERE Email = '{}' AND password = '{}' ".format(email,password)
        self.cursor.execute(user)
        self.dbconnect.commit()    

    

class Requests():
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.cursor = self.dbconnect.cursor()

    def create_request_table(self):
        request_table_create = "CREATE TABLE Requests(Request_Id serial PRIMARY KEY, UserId INT REFERENCES Users(User_Id), RequestType varchar(100) NOT NULL, RequestDetails varchar(200) NOT NULL )"
        self.cursor.execute(request_table_create)
        self.dbconnect.commit()

    def create_new_user_request(self,Id,Type,Details):
        new_request = "INSERT INTO Requests( USerId, RequestType, RequestDetails) VALUES( '{}','{}','{}')".format(Id,Type,Details) 
        self.cursor.execute(new_request)
        self.dbconnect.commit()



    def view_all_requests(self):
        requests = "SELECT * FROM Requests"
        self.cursor.execute(requests)
        self.dbconnect.commit()

    def all_requests_for_specific_user(self,userId):
        requests = "SELECT * FROM Requests WHERE UserId = '{}' ".format(userId)
        self.cursor.execute(requests)
        self.dbconnect.commit()          
    
    def specific_request(self, requestId):
        request = "SELECT * FROM Requests WHERE Request_Id = '{}'".format(requestId)
        self.cursor.execute(request)
        self.dbconnect.commit()

    
'''if __name__ == '__main__':
    User_table = USERS()
    Request_table = Requests() '''

    

 

    
