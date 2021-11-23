import sqlite3
def create_database():
    with sqlite3.connect('data folder/cafe.sqlite3') as cr:
        cr.execute("""CREATE TABLE IF NOT EXISTS stores (
   id INTEGER PRIMARY KEY,
   name  TEXT NOT NULL,
   type TEXT,
   cost_lb REAL
   	)
   """)





def drop_tables():
   with sqlite3.connect('data folder/cafe.sqlite3') as s3:
       s3.execute("DROP TABLE if exists coffees")
       s3.execute("DROP TABLE if exists specials")
       s3.execute("DROP TABLE if exists ratings")
       s3.execute("DROP TABLE if exists stores")

if __name__ == '__main__':
    create_database()

connection_handle = sqlite3.connect('data folder/cafe.sqlite3')
