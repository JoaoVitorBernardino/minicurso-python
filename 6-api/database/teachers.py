from database.db import get_connection, close_connection
import psycopg
from model.teacher import Teacher

def create_teacher(name, expertise):
    conn = get_connection()

    if conn is None:
        return
      
    try:
        with conn.cursor() as cur:
            cur.execute("insert into teachers (name, expertise) values (%s, %s) returning id", (name, expertise))

            id = cur.fetchone()[0]
            conn.commit()

            return id
    except psycopg.Error as e:
        return e
    finally:
        close_connection(conn)

def find_teachers():
    conn = get_connection()

    if conn is None:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("select * from teachers")
            rows = cur.fetchall()
            
            teachers = [Teacher(id=row[0], name=row[1], expertise=row[2]) for row in rows]

            return teachers
    except psycopg.Error as e:
        return e
    finally:
        close_connection(conn)

def find_teacher_by_id(id):
    conn = get_connection()

    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("select * from teachers where id = %s", [id])
            row = cur.fetchone()

            if row:
                return Teacher(id=row[0], name=row[1], expertise=row[2])
            else:
                return None
    except psycopg.Error as e:
        return e
    finally:
        close_connection(conn)
    

def update_teacher(id, name, expertise):
    conn = get_connection()
    
    if conn is None:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("update teachers SET name = %s, expertise = %s WHERE id = %s returning id, name, expertise", (name, expertise, id))

            row = cur.fetchone()
            
            conn.commit()

        if row:
            return Teacher(id=row[0], name=row[1], expertise=row[2])
        else:
            return None
    except psycopg.Error as e:
        return e
    finally:
        close_connection(conn)

def delete_teacher(id):
    conn = get_connection()
    
    if conn is None:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("delete from teachers where id = %s returning id", [id])

            deleted_row =  cur.fetchone()

            conn.commit()

            return deleted_row
    except psycopg.Error as e:
        return e
    finally:
        close_connection(conn)