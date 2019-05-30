import psycopg2
import datetime
from notifawards import showwindow
from contextlib import closing

class ManageSS:
    def addmember(self): 
        #with closing(psycopg2.connect(dbname='database', user='db_user', 
         #               password='mypassword', host='localhost')) as conn:
          #  with conn.cursor() as cursor:
           #     cursor.execute('SELECT * FROM airport LIMIT 5')
        print('hi')

    def exportinfo(self):
        pass

    def notifawards():
        if datetime.date.today().day == 27:
            showwindow()

if __name__=='__main__':
    ManageSS.notifawards()