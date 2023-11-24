import mysql.connector

def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='MotDePasseDeFou@123', port='3306',
                                      database='braintraining_forstudents', buffered=True, autocommit=True)

def close_dbconnection():
    db_connection.close()


def get_user_id(nickname):
    cursor = db_connection.cursor()
    query = "SELECT id FROM users WHERE nickname = %s"
    cursor.execute(query, (nickname, ))
    result = cursor.fetchone()[0]
    return result


def save(start_date, duration, nbtrials, nbsuccess, nickname, idexercise):
    query = "INSERT INTO users (nickname) VALUES (%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (nickname,))
    cursor.close()

    user_id = get_user_id(nickname)

    query = "INSERT INTO attemps (start_date, timer, nb_ok, nb_total, game_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (start_date, duration, nbsuccess, nbtrials, idexercise, user_id))
    cursor.close()


def get_result():
    for i in range(1, 1000):
        cursor = db_connection.cursor()
        cursor.execute("SELECT start_date FROM attemps WHERE id = %s", (i,))
        row = cursor.fetchone()
        if row:
            formatted_date = row[0].strftime('%Y-%m-%d')
            print(formatted_date)
    cursor.close()


open_dbconnection()