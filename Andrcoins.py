from shapito import Andrcoins
import sqlite3

conect = sqlite3.connect("finans_piromida.db")

cursr = conect.cursor()

count = cursr.execute("""INSERT INTO Andrcoins(Name,balance) VALUES
                (?,?)""", ("Pupsy iz discordica", 10))

conect.commit()
conect.close()

con = sqlite3.connect("finans_piromida.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM Andrcoins""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)

con.close()