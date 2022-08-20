import psycopg2


class DatabaseConfig:
    def __init__(self, database, user, password):
        self.database = database
        self.user = user
        self.password = password

    def table_creation(self, table_name, table_columns):
    # 1. Функция, создающая структуру БД (таблицы):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({table_columns});""")
            conn.commit()
        conn.close()

    def table_removal(self, table_name):
    # Функция, удаляющая структуру БД (таблицы):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f"""DROP TABLE {table_name};""")
            conn.commit()
        conn.close()

    def new_client(self, client_name, client_surname, client_email):
    # 2. Функция, позволяющая добавить нового клиента
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO client(name, sur_name, email) VALUES (%s, %s, %s);""", (client_name, client_surname, client_email))
            conn.commit()
        conn.close()

    def phone_adding(self, client_id, client_phone):
    # 3. Функция, позволяющая добавить телефон для существующего клиента
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO client_contacts(client_id, phone) VALUES (%s, %s);""", (client_id, client_phone))
            conn.commit()
        conn.close()

    def client_editor(self, client_name, client_surname, client_email, client_id):
    # 4. Функция, позволяющая изменить данные о клиенте
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""UPDATE client SET name = %s, sur_name = %s, email = %s WHERE id = %s;""", (client_name, client_surname, client_email, client_id))
            conn.commit()
        conn.close()

    def contacts_removal(self, contact_id):
    # 5. Функция, позволяющая удалить телефон для существующего клиента
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""DELETE FROM client_contacts WHERE id=%s;""", (contact_id))
            conn.commit()
        conn.close()

    def client_removal(self, client_id):
    # 6. Функция, позволяющая удалить клиента
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute("""DELETE FROM client WHERE id=%s;""", (client_id))
            conn.commit()
        conn.close()

    def client_search(self, search):
    # 7. Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        with conn.cursor() as cur:
            cur.execute(f"""SELECT name, sur_name, email, phone FROM client c JOIN client_contacts ct ON c.id = ct.client_id WHERE name LIKE '%{search}%' OR sur_name LIKE '%{search}%' OR email LIKE '%{search}%' OR phone LIKE '%{search}%';""")
            return print(cur.fetchall())
        conn.close()