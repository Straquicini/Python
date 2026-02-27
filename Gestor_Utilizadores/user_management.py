import sqlite3
from users import User

class UserManagement:
    def __init__(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS users_tb(
                    id integer primary key autoincrement,
                    nome text not null,
                    username text unique not null,
                    password text not null,
                    email text unique not null
                )
            """
        )
        
        conn.commit()
        conn.close()
        
    def insert(self, new_user: User):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        hashed_password = new_user.hash_password()
        
        try:
            cursor.execute(
                "INSERT INTO users_tb(nome,username,password,email) VALUES (?,?,?,?)",
                (new_user.nome,new_user.username,hashed_password,new_user.email)
            )
            conn.commit()
            print("Utilizador inserido com sucesso!")
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir o novo utilizador: {e}")
        finally:
            conn.close()

    def find_username(self,username_to_find):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id, nome, username, email FROM users_tb WHERE username = ?",
            (username_to_find,)
        )
        u = cursor.fetchone()
        conn.close()
        
        if u:
            print("Utilizador encontrado!")
            user = User(u[1],u[2],u[3],u[4])
            return user
        else:
            print("Utilizador não encontrado!")
            return None
        
    def delete(self, user: User):
        if self.find_username(user) is None:
            print("Urilizador inexistente")
        else:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
        
            try:
                cursor.execute(
                    "DELETE FROM users_tb WHERE username = ?",
                    (user.username,)
                )
                conn.commit()
                print(f"Utilizador {user.username} eliminado com sucesso!")       
            except sqlite3.IntegrityError as e:
                print(f"Erro ao eliminar utilizador: {e}")
            finally:
                conn.close()

        
  
        