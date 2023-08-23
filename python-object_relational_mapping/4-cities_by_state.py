#!/usr/bin/python3
''' Lists all cities from the database hbtn_0e_4_usa '''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cr = db.cursor()
    cr.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    cities = cr.fetchall()
    for city in cities:
        print(city)
    cr.close()
    db.close()
