import sqlite3

def create_connection(db_file):
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_file)
        return db_connection
    except sqlite3.Error as db_error:
        print(db_error)

def create_table(db_connection, create_table_sql):
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as db_error:
        print(db_error)
    # finally:
    #     db_connection.close()    

def create_record(db_connection, korisnik):
    print(korisnik)
    try:
        sq_query = ''' INSERT INTO korisnici(pin, ime, prezime, aktivan)
                VALUES(?, ?, ?, ?) '''
        cursor = db_connection.cursor()
        cursor.execute(sq_query, korisnik)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()

def update_record(db_connection, korisnik):
    try:    
        sql = ''' UPDATE Korisnici
                SET ime = ? ,
                    prezime = ?,
                    aktivan = ?
                WHERE pin = ?'''
        cursor = db_connection.cursor()
        cursor.execute(sql, korisnik)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()

def delete_record(db_connection, id):
    try:
        sql = 'DELETE FROM Korisnici WHERE pin=?'
        cursor = db_connection.cursor()
        cursor.execute(sql, (id,))
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()

def delete_all_records(db_connection):
    try:
        sql = 'DELETE FROM Korisnici'
        cursor = db_connection.cursor()
        cursor.execute(sql)
        db_connection.commit()
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()

def select_all_records(db_connection):
    try:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM Korisnici")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()
        

def select_record_by_id(db_connection, id):
    try:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM Korisnici WHERE pin=?',(id,)) 
        rows = cursor.fetchall()
        for row in rows:
            return row
    except sqlite3.Error as db_error:
           print(db_error)
    finally:
        db_connection.close()













