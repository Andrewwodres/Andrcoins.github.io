import sqlite3

con = sqlite3.connect("finans_piromida.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM Andrcoins""").fetchall()
# Вывод результатов на экран

print("Content-type: text/html")
f = open("README.md", 'w')
print(f.write('<h1 align="center">Andrcoins owners</h1>'))
for elem in result:
    print(f.write(f"<h2 align='center'>{': '.join(map(str, elem))}</h2> \n"))
con.close()
