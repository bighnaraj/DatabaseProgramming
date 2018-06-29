import psycopg2

def create():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='myPassword' host='localhost'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='myPassword' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store values('%s','%d','%f')" %(item,quantity,price))
    conn.commit()
    conn.close()

create()
#insert("glass",25,15.5)

def view():
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='myPassword' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def update(quantity,item):
    conn = psycopg2.connect("dbname='postgres' user='postgres' password='myPassword' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s WHERE item=%s",(quantity,item))
    conn.commit()
    conn.close()

update(23,'glass')

print(view())
