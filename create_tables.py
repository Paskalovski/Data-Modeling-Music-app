import psycopg2
from queries import create_table_queries, drop_table_queries


def create_database():
    """
    function: return's (cur, conn) a cursor and connection reference
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=password")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # creating the sparkify database
    cur.execute("DROP DATABASE IF EXISTS musicapp")
    cur.execute("CREATE DATABASE musicapp WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    # connecting to the sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=musicapp user=postgres password=password")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    print("Tables dropped successfully!!")

    create_tables(cur, conn)
    print("Tables created successfully!!")

    conn.close()


if __name__ == "__main__":
    main()