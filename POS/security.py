
class Security:
    def __init__(self,admin_manage,user_manage=None):
        self.am= admin_manage
        self.um = user_manage
    def authenticate_admin(self,mail,password):
        response = self.am.verifyAdmin(mail,password)
        if response['value']:
            if response['data']:
                return {"value": True,"message": "User authentication successfully","data": response['data'][0]}
            else:
                return {"value": False,"message":"Invalid email id combination","data": None}
        else:
            return {"value": False,"message":response['message'],"data":None}
    def authenticate_user(self,mail,password):
        response = self.um.verifyUser(mail,password)
        if not response['value']: 
                return {"value": False,"message":response['message'],"data": None}
        if response['data']:
            return {"value": True,"message":"Authentication Successfull","data": response['data'][0]}
        else:
            return {"value": False,"message":"Invalid email id combination","data": None}