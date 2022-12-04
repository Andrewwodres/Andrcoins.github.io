import sqlite3

con = sqlite3.connect("finans_piromida.db")

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT after, time, name FROM operationss""").fetchall()
# Вывод результатов на экран
a = []
for i in result:
    a = []
    print(i)
    names = ''.join(i[2].split())
    f = open(f"gays/{names}.html", 'r')
    for number, line in enumerate(f):
        a.append(line.strip())
    f = open(f"gays/{names}.html", 'w')
    b, t, n = i
    a.append("<h2 align='center'>" + n + str(b) + t + '</h2>'.strip())
    f.seek(0)
    print(a)
    for iss in a:
        f.write(f"{iss}"+ '\n')
con.close()