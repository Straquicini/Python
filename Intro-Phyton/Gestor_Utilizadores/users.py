import hashlib

class User:
    def __init__(self,nome,username,passwd,email):
        self.__nome = nome
        self.__username =username
        self.__passwd = passwd
        self.__email = email
        
    def __str__(self):
        return f"{self.__username}" ({self.__email})
    
    # getters
    @property
    def nome(self): return self.__nome
    @property
    def username(self): return self.__username
    @property
    def passwd(self): return self.__passwd
    @property
    def email(self): return self.__email
    
    # setters
    @nome.setter
    def nome(self,nome_alterado): self.__nome = nome_alterado
    @passwd.setter
    def passwd(self,passwd_alterada): self.__passwd = passwd_alterada
    @email.setter
    def email(self,email_alterado): self.__email = email_alterado
    
    # Função para encriptar a password
    def hash_password(self):
        return hashlib.sha256(self.__passwd.encode()).hexdigest()
    
    # Verifica se a password escrita é igual a pass armazenada
    def verify_password(self, password_armazenada):
        return self.__passwd == password_armazenada