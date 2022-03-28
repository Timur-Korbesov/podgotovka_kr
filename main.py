import sqlite3

name_bd = input()
min_size = int(input())
max_rate = int(input())


# Подключение к БД
con = sqlite3.connect(name_bd)

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
quare = f"""SELECT streelers.size
            FROM streelers
            WHERE size >= {min_size} and rate <= {max_rate}"""

result = cur.execute(quare).fetchall()

ans = []
for el in result:
    query = "select name from colors where id == ?"
    start_color = cur.execute(query, (el[1], )).fetchone()[0]
    end_color = cur.execute(query, (el[2], )).fetchone()[0]
    ans.append((start_color, end_color, el[0]))

con.close()
ans.sort(key=lambda x: (x[2], x[0], x[1]))

for i in ans:
    print(*i)