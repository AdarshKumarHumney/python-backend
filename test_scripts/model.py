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
        return self.ConvertToDic(search_list,colums)
    def printUser(self,choice):
        found_list = self.database.PrintTable(choice)
        return found_list
    def UpdateTable(self,table,field,field_value,id_value):
        return self.database.UpdateDatabase(table,field,field_value,id_value)
    def DeleteTable(self,table,id):
        return self.database.DeleteDatabase(table,id)
class AdminUser(People):
    def __init__(self, database):
        super().__init__(database)
        self.rows = ["id","name","email","password"]
        self.table = "admin"
    def AddAdmin(self,name,email,password):
        self.database.InserIntoAdmin(name,email,password)
    def SearchAdmin(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def PrintList(self):
        return super().ConvertToDic(super().printUser(self.table),self.rows)
    def UpdateAdmin(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def DeleteAdmin(self,id):
        return super().DeleteTable(self.table,id)
class NormalUser(People):
    def __init__(self, database):
        super().__init__(database)
        self.table = "user"
        self.rows = ["id","name","email","age"]
    def InsertUser(self,name,email,age):
        return self.database.InsertIntoUser(name,email,age)
    def SearchUser(self,choice,value):
        return super().SearchTable(self.table,choice,value,self.rows)
    def UpdateUser(self,field,field_value,id_value):
        return super().UpdateTable(self.table,field,field_value,id_value)
    def PrintList(self):
        return self.ConvertToDic(super().printUser(self.table),self.rows)
    def DeleteUser(self,id):
        return super().DeleteTable(self.table,id)
