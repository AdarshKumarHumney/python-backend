class People:
    def __init__(self,database):
        self.database = database
    def ConvertToDic(self,list1,rows):
        result = []
        for i in list1:
            convert = dict(zip(rows,i))
            result.append(convert)
        return result
    def SearchTable(self,table,field,value,colums):
        search_list = self.database.searchDataBase(table,field,value)
        if search_list['value']:
            return {"value":True,"message":search_list['message'],"data":self.ConvertToDic(search_list['data'],colums)}
        else:
            return {"value":False,"message":search_list['message'],"data":None}
    def printUser(self,choice):
        found_list = self.database.PrintTable(choice)
        return found_list
    def UpdateTable(self,table,field,field_value,id_value):
        return self.database.UpdateDatabase(table,field,field_value,id_value)
    def DeleteTable(self,table,id): 
        return self.database.DeleteDatabase(table,id)
class AdminUser(People):
    REQUIRED_FIELDS = {
        "name":str,
        "email":str,
        "password":str
    }
    def __init__(self, database):
        super().__init__(database)
        self.rows = ["id","name","email","password"]
        self.table = "admin"
        self.role = "Admin"
    def SaveUser(self,data):
        return self.database.InsertIntoAdmin(data['name'],data['email'],data['password'])
    def SearchUser(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def PrintList(self):
        return super().ConvertToDic(super().printUser(self.table),self.rows)
    def UpdateUser(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def DeleteUser(self,id):
        return super().DeleteTable(self.table,id)
class NormalUser(People):
    REQUIRED_FIELDS={
        "name":str,
        "email":str,
        "age":int
    }
    def __init__(self, database):
        super().__init__(database)
        self.table = "user"
        self.rows = ["id","name","email","age"]
        self.role = "User"
    def SaveUser(self,data):
        return self.database.InsertIntoUser(data['name'],data['email'],data['age'])
    def SearchUser(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def UpdateUser(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def PrintList(self):
        return self.ConvertToDic(super().printUser(self.table),self.rows)
    def DeleteUser(self,id):
        return super().DeleteTable(self.table,id)
