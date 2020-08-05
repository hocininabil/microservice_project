
'''
@author: nabil
'''

import pymysql
import sys
class Database:
    def connect(self):
        return pymysql.connect("ue-mysql","dev","root","crud_flask_ue" )

    def get_ue_info(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM ue order by nom asc")
            else:
                cursor.execute("SELECT * FROM ue where id = %s order by nom asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,nom,des,res):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            print("entered")
            cursor.execute("INSERT INTO ue(nom,description,responsable) VALUES(%s, %s, %s)", (nom,des,res,))
            con.commit()

            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, nom):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM ue where nom = %s", (nom,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
