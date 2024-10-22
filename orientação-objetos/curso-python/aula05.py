#Métodos de Classe e Métodos estáticos
class Connection:
   def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
      
   def set_user(self, user):
        self.user = user
   
   def set_password(self, password):
        self.password = password

   @classmethod
   def connect_client(cls, user, password):
        client = cls()
        client.set_user(user)
        client.set_password(password)
        return client


cc = Connection.connect_client('user', 'password')
print(cc.user)