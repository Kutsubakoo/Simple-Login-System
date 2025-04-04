import psycopg2

db_name = "RegisteredAccountsDB"
db_user = "postgres"
db_pw = "angelo"
db_host = "localhost"

def CreateTable():
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS RegisteredAccounts (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL)')
    conn.commit()
    cur.close()
    conn.close()

def CreateAcc(username, password):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('INSERT INTO public.registeredaccounts(username, password) VALUES (%s, %s)', (username, password))
    conn.commit()
    cur.close()
    conn.close()

def CheckCredentials(username, password):
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host)
    cur = conn.cursor()
    query = """
        SELECT EXISTS (
            SELECT 1
            FROM public.registeredaccounts
            WHERE (username = %s AND password = %s)
        );
    """
    cur.execute(query, (username, password))
    conn.commit()
    is_registered = cur.fetchone()
    is_correct = is_registered[0]
    cur.close()
    conn.close()
    return is_correct

