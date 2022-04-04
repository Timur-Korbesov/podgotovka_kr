import sqlite3


class SnowRace:
    def __init__(self, name_bd):
        self.name_bd = name_bd

    def race_members(self, date_begin, point_start):
        con = sqlite3.connect(self.name_bd)
        cur = con.cursor()
        ans = []
        result1 = cur.execute("SELECT trip_id FROM trips WHERE start_point = ? AND start_date = ?",
                              (point_start, date_begin)).fetchone()
        result2 = cur.execute("SELECT person_id FROM members WHERE trip_id = ?", (result1[0],)).fetchall()
        for el in result2:
            result = cur.execute("SELECT surname, name FROM participants WHERE id = ?", (el[0],)).fetchall()
            ans.append(result[0][0] + " " + result[0][1])
        return ans

    def visited(self, surname):
        con = sqlite3.connect(self.name_bd)
        cur = con.cursor()
        res1 = cur.execute("SELECT id FROM participants WHERE surname = ?", (surname,)).fetchone()
        res2 = cur.execute("SELECT trip_id FROM members WHERE person_id = ?", (res1[0],)).fetchall()
        otvet = []

        for el in res2:
            response = cur.execute("""SELECT start_point, end_point FROM trips WHERE trip_id = ?""", (el[0],)).fetchall()
            otvet.append(response[0][0])
            otvet.append(response[0][1])
        otvet = list(set(otvet))
        return sorted(otvet)


sr = SnowRace("race.db")
print(*sr.visited("Fogg"), sep="\n")