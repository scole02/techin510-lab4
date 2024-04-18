import time
import psycopg2

class Database:
    def __init__(self, database_url) -> None:
        self.con = psycopg2.connect(database_url)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def create_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS quotes (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            tags TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.cur.execute(q)
        self.con.commit()

    def truncate_table(self):
        q = """
        TRUNCATE TABLE quotes
        """
        self.cur.execute(q)
        self.con.commit()
    
    def insert_quote(self, quote):
        q = """
        INSERT INTO quotes (content, author, tags) VALUES (%s, %s, %s)
        """
        self.cur.execute(q, (quote['content'], quote['author'], quote['tags'],))
        self.con.commit()