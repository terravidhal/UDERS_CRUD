# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


# model the class after the users table from our database
class Users:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data["idusers"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"].strftime("%B %drd %Y %H:%M:%S %p")
        self.updated_at = data["updated_at"].strftime("%B %drd %Y %H:%M:%S %p")

    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        # print("results :", results)
        users_Arr = []
        for one_user in results:
            users_Arr.append(cls(one_user))
            print(cls(one_user))
        return users_Arr
    

    @classmethod
    def create_user(cls, datas):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(eml)s, NOW(), NOW());"
        results = connectToMySQL(cls.DB).query_db(query, datas)
        # print("results :", results) # results == id du user crée
        user_id_created = results
        return user_id_created 

    # READ
    # ONE elt
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM users WHERE idusers = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
       # print('new results:++', results)
        return cls(results[0])

    # UPDATE
    @classmethod
    def update(cls,data):
        query = """UPDATE users 
                SET first_name=%(fname)s, last_name=%(lname)s, email=%(eml)s , updated_at = NOW() 
                WHERE idusers = %(id)s;"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print('result+++:',result) 
        return result
    

    # DELETE        
    @classmethod
    def delete(cls, data):
        query  = "DELETE FROM users WHERE idusers = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print('result+++:',result) 
        return result