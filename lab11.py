import sqlite3 

conn = sqlite3.connect("lab11.db")
c = conn.cursor()

f = open("score2.txt").read().strip()
lines = [x.strip() for x in f.split("\n")]

c.execute("PRAGMA foreign_keys = ON")
c.execute('''CREATE TABLE IF NOT EXISTS persons(
            id INTEGER PRIMARY KEY,
            firstName TEXT,
            lastName TEXT,
            UNIQUE(firstName, lastName) ON CONFLICT IGNORE
            );''')

c.execute('''CREATE TABLE IF NOT EXISTS scores(
            personID INTEGER,
            taskNr INTEGER,
            points INTEGER,
            FOREIGN KEY (personID) REFERENCES persons(id) ON DELETE CASCADE
            );''')



# for line in lines:
#     name = line.split(" ")
#     c.execute('INSERT INTO persons (firstName, lastName) VALUES (?,?);', (name[2], name[3]))
#     print("{} {}".format(name[2], name[3]))

# for line in lines:
#     taskAndPoint = line.split(" ")
#     for personID in c.execute("SELECT id FROM persons WHERE firstName = ? AND lastName = ?", (taskAndPoint[2], taskAndPoint[3])):
#         c.execute("INSERT INTO scores (personID, taskNr, points) VALUES (?,?,?)", (personID[0], taskAndPoint[1], taskAndPoint[4]))
#         break



# Query 1
query1 = c.execute("""SELECT firstName||' '||lastName as Name, sum(points) as points FROM persons
                    JOIN scores on scores.personID = persons.id
                    GROUP by id
                    ORDER BY sum(points) DESC 
                    LIMIT(10)""").fetchall() 


query2 = c.execute("""SELECT taskNr FROM scores
                    GROUP BY taskNr 
                    ORDER BY sum(points) ASC
                    LIMIT(10)""").fetchall()

def printQuery1():
    print(query1)

def printQuery2():
    print(query2)

def printPersonsTable():
    for row in c.execute("SELECT * FROM persons"):
        print(row)

def printScoresTable():
    for row in c.execute("SELECT * FROM scores"):
        print(row)

conn.commit()
conn.close()
