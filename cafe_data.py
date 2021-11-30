import sqlite3
def create_database():
    with sqlite3.connect('data folder/cafe.sqlite3') as cr:
        cr.execute("""CREATE TABLE IF NOT EXISTS stores (
   id INTEGER PRIMARY KEY,
   name  TEXT NOT NULL,
   type TEXT,
   volume INTEGER
   	)
   """)
    cr.execute("""CREATE TABLE IF NOT EXISTS specials (
       id INTEGER PRIMARY KEY,
       date TEXT NOT NULL,
       store_name TEXT,
       coffee_name TEXT,
       cost_lb REAL
       	)
       """)
    cr.execute("""CREATE TABLE IF NOT EXISTS ratings (
           id INTEGER PRIMARY KEY,
           date TEXT NOT NULL,
           store_name TEXT,
           rating INTEGER
           	)
           """)
    cr.execute("""CREATE TABLE IF NOT EXISTS coffees (
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              type TEXT,
              cost_lb REAL
              	)
              """)
    cr.execute("CREATE UNIQUE INDEX stores_name_index ON stores(name)")
    cr.execute("CREATE INDEX stores_name_specials ON specials(store_name)")
    cr.execute("CREATE INDEX stores_name_ratings ON ratings(store_name)")
    cr.execute("CREATE UNIQUE INDEX coffeename_coffees ON coffees(name)")






def drop_tables():
   with sqlite3.connect('data folder/cafe.sqlite3') as s3:
       s3.execute("DROP TABLE if exists coffees")
       s3.execute("DROP TABLE if exists specials")
       s3.execute("DROP TABLE if exists ratings")
       s3.execute("DROP TABLE if exists stores")

if __name__ == '__main__':
    create_database()


