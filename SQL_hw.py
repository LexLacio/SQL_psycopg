import configparser

from SQL_hw_engine import DatabaseConfig

config = configparser.ConfigParser()
config.read("settings.ini")

db_name = config["Database"]["db_name"]
user_name = config["Database"]["user_name"]
user_password = config["Database"]["user_password"]

new_db = DatabaseConfig(db_name, user_name, user_password)

# # Функция, удаляющая структуру БД (таблицы):
# new_db.table_removal('client_contacts')
# new_db.table_removal('client')

# # 1. Функция, создающая структуру БД (таблицы):
# new_db.table_creation('client', 'id SERIAL PRIMARY KEY, name VARCHAR(20), sur_name VARCHAR(20), email VARCHAR(40) UNIQUE NOT NULL')
# new_db.table_creation('client_contacts', 'id SERIAL PRIMARY KEY, client_id INTEGER NOT NULL REFERENCES client(id), phone VARCHAR(40)')
#
# # 2. Функция, позволяющая добавить нового клиента
# new_db.new_client('Иван', 'Иванов', 'ivan@mail.ru')
# #
# # 3. Функция, позволяющая добавить телефон для существующего клиента
# new_db.phone_adding('1', '+7(495)555-55-55')
#
# # 4. Функция, позволяющая изменить данные о клиенте
# new_db.client_editor("Петр", "Сидоров", "123@mail.ru", "1")

# #  5.Функция, позволяющая удалить телефон для существующего клиента
# new_db.contacts_removal('1')

# # 6. Функция, позволяющая удалить существующего клиента
# new_db.client_removal('1')

# # 7. Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
# new_db.client_search('Пет')



