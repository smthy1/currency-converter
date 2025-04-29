import sqlite3
from datetime import date

today = date.today()


def connect():
    conn = sqlite3.connect('Exchange_Rate.db')
    cursor = conn.cursor()
    connection = (conn, cursor)
    return connection


def create_table():
    try:
        conn, cursor = connect()
        cursor.execute('''CREATE TABLE IF NOT EXISTS exchange_rate(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            currency_base TEXT NOT NULL,
                            currency_target TEXT NOT NULL,
                            quotation REAL,
                            last_update TEXT)''')
        conn.commit()

    except sqlite3.Error as error:
        print(f'Error creating table: {error}')

    finally:
        conn.close()


def add_record(currency_base, currency_target, quotation, last_update=today):
    try:
        conn, cursor = connect()
        cursor.execute('''
                INSERT INTO exchange_rate(currency_base, currency_target, quotation, last_update) VALUES (
                       ?, ?, ?, ?)''', (currency_base, currency_target, quotation, last_update))
        conn.commit()
    
    except sqlite3.Error as error:
        print(f'Error add record: {error}')

    finally:
        conn.close()


def records_list():
    try:
        conn, cursor = connect()
        cursor.execute("SELECT * FROM exchange_rate")
        records = cursor.fetchall()
        if not records:
            print('None records yet.')
            return
        
        print('\nRecords list')
        print('-'*100)

        for record in records:
            print(f"ID: {record[0]} | Currency Base: {record[1]} | Currency Target: {record[2]} | "
                  f"Quotation: {record[3]} | Last Update: {record[4]}")
            print('-'*100)
    except sqlite3.Error as error:
        print(f"Error listing records: {error}")
    
    finally:
        conn.close()