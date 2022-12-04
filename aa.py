import sqlite3
def nice():
    m = []
    con = sqlite3.connect("finans_piromida.db")

        # Создание курсора
    cur = con.cursor()

        # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT * FROM Andrcoins""").fetchall()
        # Вывод результатов на экран

    print("Content-type: text/html")
    for elem in result:
        i, n, b = elem
        m.append((n, b))
    con.close()
    return m

print(nice())