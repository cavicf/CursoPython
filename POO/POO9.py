# #method vs @classmethod vs @staticmethod
# method - self, método de instancia (objeto)
# @classmethod - cls, método de classe 
# @staticmethod - método estático (xself, xcls)

class Connection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        #método setter - usado para configurar o valor de algo
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)

    def connection_log(msg):
        print('LOG:', msg)

#c1 = Connection()
c1 = Connection.create_with_auth('Luiz', '1234')
# c1.set_user('Luiz')
# c1.set_password('123')
print(Connection.log('essa é a msg de log'))
print(c1.user)
print(c1.password)

        