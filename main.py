import random
import mysql.connector
import requests


def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP="http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl += "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl += "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl += "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode

voteSchere = 0
voteStein = 0
votePapier = 0
voteEchse = 0
voteSpock = 0

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sspes"
)

mycursor = mydb.cursor()

dic = {"stein": 0, "papier": 1, "schere": 2, "echse": 3, "spock": 4}

print("\n=======---Stein, Papier, Schere, Echse, Spock---=======\n")
print("Stein schleift Schere und zerquetscht Echse.")
print("Papier bedeckt Stein und widerlegt Spock.")
print("Schere schneidet Papier und köpft Echse.")
print("Echse frisst Papier und vergiftet Spock.")
print("Spock zertrümmert Schere und verdampft Stein.\n")
print(55 * "=")

while True:

    while True:
        wahl = input("Nun wähle! Aber wähle weise: ")
        wahl = wahl.lower()

        if wahl not in dic.keys():
            print("Falsche Eingabe! Nochmal!\n")

        else:
            ai = random.choice(list(dic.keys()))
            ai = ai.lower()

            sql = "INSERT INTO sspes (spieler, npc) VALUES (%s, %s)"
            val = (wahl, ai)
            mycursor.execute(sql, val)
            mydb.commit()
            break

    if wahl == ai:
        print("{0:10}{1:10}".format("Spieler: ", wahl[0].upper() + wahl[1:]))
        print("{0:10}{1:10}".format("Computer: ", ai[0].upper() + ai[1:]))
        print("Unentschieden!")

    elif (
            (wahl == "stein" and (ai == "schere" or ai == "echse")) or
            (wahl == "papier" and (ai == "stein" or ai == "spock")) or
            (wahl == "schere" and (ai == "papier" or ai == "echse")) or
            (wahl == "echse" and (ai == "papier" or ai == "spock")) or
            (wahl == "spock" and (ai == "stein" or ai == "schere"))
    ):
        print("{0:10}{1:10}".format("Spieler: ", wahl[0].upper() + wahl[1:]))
        print("{0:10}{1:10}".format("Computer: ", ai[0].upper() + ai[1:]))
        print("Du gewinnst!")

        sql = "INSERT INTO hs (spielergewonnen, npcgewonnen) VALUES (%s, %s)"
        val = (True, False)
        mycursor.execute(sql, val)
        mydb.commit()

    else:
        print("{0:10}{1:10}".format("Spieler: ", wahl[0].upper() + wahl[1:]))
        print("{0:10}{1:10}".format("Computer: ", ai[0].upper() + ai[1:]))
        print("Der Computer gewinnt!")

        sql = "INSERT INTO hs (spielergewonnen, npcgewonnen) VALUES (%s, %s)"
        val = (False, True)
        mycursor.execute(sql, val)
        mydb.commit()

    show = input("\nSoll die Statistik ausgegeben werden? (j/n): ")
    if show == "j" or show == "n":
        print("Der Spieler hat so oft Spock genommen:")
        voteSpock = mycursor.execute('SELECT count(spieler) FROM sspes where spieler = "spock";')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("Der Spieler hat so oft Schere genommen:")
        voteSchere = mycursor.execute('SELECT count(spieler) FROM sspes where spieler = "schere";')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("Der Spieler hat so oft Stein genommen:")
        voteStein = mycursor.execute('SELECT count(spieler) FROM sspes where spieler = "stein";')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("Der Spieler hat so oft Papier genommen:")
        votePapier = mycursor.execute('SELECT count(spieler) FROM sspes where spieler = "papier";')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("Der Spieler hat so oft Echse genommen:")
        voteEchse = mycursor.execute('SELECT count(spieler) FROM sspes where spieler = "echse";')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("Der Computer hat so oft Spock genommen:")
        temp = mycursor.execute('SELECT count(npc) FROM sspes where npc = "spock";')
        myresult = mycursor.fetchall()
        voteSpock = voteSpock + temp

        for x in myresult:
            print(x)

        print("Der Computer hat so oft Schere genommen:")
        temp = mycursor.execute('SELECT count(npc) FROM sspes where npc = "schere";')
        myresult = mycursor.fetchall()
        voteSchere = voteSchere + temp

        for x in myresult:
            print(x)

        print("Der Cmputer hat so oft Stein genommen:")
        temp = mycursor.execute('SELECT count(npc) FROM sspes where npc = "stein";')
        myresult = mycursor.fetchall()
        voteStein = voteStein + temp

        for x in myresult:
            print(x)

        print("Der Computer hat so oft Papier genommen:")
        temp = mycursor.execute('SELECT count(npc) FROM sspes where npc = "papier";')
        myresult = mycursor.fetchall()
        votePapier = votePapier + temp

        for x in myresult:
            print(x)

        print("Der Computer hat so oft Echse genommen:")
        temp = mycursor.execute('SELECT count(npc) FROM sspes where npc = "echse";')
        myresult = mycursor.fetchall()
        voteEchse = voteEchse + temp

        for x in myresult:
            print(x)

        print("So oft hat der Spieler gewonnen:")
        mycursor.execute("SELECT count(spielergewonnen) FROM hs")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        print("so oft hat der Computer gewonnen:")
        mycursor.execute("SELECT count(npcgewonnen) FROM hs")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    again = input("\nNochmal (j/n): ")
    if again == "J" or again == "j":
        continue
    else:
        print(sendRequest("Achulleus", voteSchere, voteStein, votePapier, voteSpock, voteEchse))
        mydb.close()
        break

