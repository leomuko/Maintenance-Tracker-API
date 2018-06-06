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
        user = "SELECT Email, password FROM Users WHERE Email = '{}' AND password = '{}' ".format(email,password)
        self.cursor.execute(user)
        user_data = self.cursor.fetchall()
        user_list =[]
        user_dictionary ={}
        for i in user_data:
            user_dictionary['Email'] = i[0]
            user_dictionary['password'] = i[1] 
            user_list.append(user_dictionary)   
            user_dictionary = {}
        return user_list

    def get_user_Id(self,Email):
        user = "SELECT User_Id FROM Users WHERE Email = '{}'".format(Email)
        self.cursor.execute(user)
        user_id = self.cursor.fetchall()
        for i in user_id:
            USERID = i
        return USERID    




class Requests():
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.cursor = self.dbconnect.cursor()

    def create_request_table(self):
        request_table_create = "CREATE TABLE Requests(Request_Id serial PRIMARY KEY, UserId INT REFERENCES Users(User_Id), RequestType varchar(100) NOT NULL, RequestDetails varchar(200) NOT NULL, Status varchar(100) )"
        self.cursor.execute(request_table_create)
        self.dbconnect.commit()

    def create_new_user_request(self,Id,Type,Details):
        new_request = "INSERT INTO Requests( USerId, RequestType, RequestDetails) VALUES( '{}','{}','{}')".format(Id,Type,Details) 
        self.cursor.execute(new_request)
        self.dbconnect.commit()



    def view_all_requests(self):
        requests = "SELECT * FROM Requests"
        self.cursor.execute(requests)
        all_requests = self.cursor.fetchall()
        
        request_dictionary = {}
        request_List = []
        for i in all_requests:
            request_dictionary['request_Id'] = i[0]
            request_dictionary['userId'] = i[1]
            request_dictionary['requestType'] = i[2]
            request_dictionary['details'] = i[3]
            request_dictionary['status'] = i[4]
            request_List.append(request_dictionary)
            request_dictionary ={}
        return request_List    


    def all_requests_for_specific_user(self,userId):
        requests = "SELECT * FROM Requests WHERE UserId = '{}' ".format(userId)
        self.cursor.execute(requests)
        self.dbconnect.commit()
        request = self.cursor.fetchall()
        request_dictionary = {}
        request_list = []
        for i in request:
            request_dictionary['request_Id'] = i[0]
            request_dictionary['userId'] = i[1]
            request_dictionary['requestType'] = i[2]
            request_dictionary['details'] = i[3]
            request_dictionary['status'] = i[4]
            request_list.append(request_dictionary)
            request_dictionary ={}
        return request_list         
    
    def specific_request(self, requestId):
        request = "SELECT * FROM Requests WHERE Request_Id = '{}'".format(requestId)
        self.cursor.execute(request)
        user_request = self.cursor.fetchall()
        request_dictionary = {}
        request_List = []
        for i in user_request:
            request_dictionary['request_Id'] = i[0]
            request_dictionary['userId'] = i[1]
            request_dictionary['requestType'] = i[2]
            request_dictionary['details'] = i[3]
            request_dictionary['status'] = i[4]
            request_List.append(request_dictionary)
            request_dictionary ={}
        return request_List

    def modify_request(self,requestId,Type,Details):
        new_request = "UPDATE Requests SET RequestType = '{}', RequestDetails = '{}' WHERE Request_Id ='{}'".format(Type,Details,requestId)
        self.cursor.execute(new_request)
        self.dbconnect.commit()


class Administrator():
    def __init__(self):
        self.dbconnect = psycopg2.connect(database="postgres", user = "postgres", password = "test123", host = "127.0.0.1", port = "5432")
        self.cursor = self.dbconnect.cursor()      

    def get_all_requests(self):
        requests = "SELECT * FROM Requests"
        self.cursor.execute(requests)
        self.dbconnect.commit()
        request = self.cursor.fetchall()
        request_dictionary = {}
        request_list = []
        for i in request:
            request_dictionary['request_Id'] = i[0]
            request_dictionary['userId'] = i[1]
            request_dictionary['requestType'] = i[2]
            request_dictionary['details'] = i[3]
            request_dictionary['status'] = i[4]
            request_list.append(request_dictionary)
            request_dictionary ={}
        return request_list   

    def view_all_users(self):
        users = "SELECT * FROM Users"
        self.cursor.execute(users)
        self.dbconnect.commit()
        all_users = self.cursor.fetchall()
        all_user_dictionary = {}
        all_user_list = []
        for i in all_users:
            all_user_dictionary['user_Id'] = i[0]
            all_user_dictionary['FirstName'] = i[1]
            all_user_dictionary['LastName'] = i[2]
            all_user_dictionary['Email'] = i[3]
            all_user_dictionary['password'] = i[4]
            all_user_list.append(all_user_dictionary)
            all_user_dictionary ={}
        return all_user_list  

    def approve_request(self,request_id):
        request = "UPDATE Requests SET Status = '{}' WHERE Request_Id = '{}'".format('Approved', request_id)      
        self.cursor.execute(request)
        self.dbconnect.commit()

    def disapprove_request(self,request_id):
        request = "UPDATE Requests SET Status = '{}' WHERE Request_Id = '{}'".format('Disapproved', request_id)      
        self.cursor.execute(request)
        self.dbconnect.commit()

    def resolve_request(self,request_id):
        request = "UPDATE Requests SET Status = '{}' WHERE Request_Id = '{}'".format('Resolved', request_id)      
        self.cursor.execute(request)
        self.dbconnect.commit()

   

    

    

 

    
