class Security:
    def __init__(self,connected):
        self.connected = connected
        self.login = False
    def LoginCheck(self,table,email,password):
        result_found = self.connected.SecurityCheck(table,"email","password",email,password)
        if result_found:
            self.login = True
            return {"login":self.login,"message":"login credentials matched"}
        else:
            return {"login":self.login,"message":"login did no matched"}
