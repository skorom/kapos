import cherrypy
import random
import mysql.connector


def randomszo():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kapos"
    )

    szam = random.randint(1, 5)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT szo FROM szavak WHERE id='" + str(szam) + "'")

    myresult = mycursor.fetchall()

    szo = ''

    for x in myresult:
        szo = x

    cherrypy.config.update({'server.socket_port': 4021})
    cherrypy.engine.restart()

    class RandomWord(object):
        @cherrypy.expose
        def index(self):
            return szo

    if __name__ == '__main__':
        cherrypy.quickstart(RandomWord())


if __name__ == '__main__':
    cherrypy.quickstart(randomszo())