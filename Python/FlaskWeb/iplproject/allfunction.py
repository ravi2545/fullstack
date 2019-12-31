import sqlite3

class iplwebsite:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()

    def database(self,u,key,val):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            ct = "CREATE TABLE IF NOT EXISTS {} (name VARCHAR(20), pass VARCHAR(20))".format(
                u)  # CREATE TABLES DYNAMICALLY IN SQLite3
            cur.execute(ct)
            cur.execute("INSERT into {}(name,pass) values (?,?)".format(u),
                        (key, val))  # INSERT VALUES DYNAMICALLY IN SQLite3
            con.commit()

