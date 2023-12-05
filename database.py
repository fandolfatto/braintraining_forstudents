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
    """
        # TODO : Vérifier que le joueur n'existe pas déjà
        if ("SELECT nickname FROM users WHERE nickname = %s"):
        print("L'utilisateur existe déjà")
        else:
        query = "INSERT INTO users (nickname) VALUES (%s)"
        cursor = db_connection.cursor()
        cursor.execute(query, (nickname,))
        cursor.close()
    """
    query = "INSERT INTO users (nickname) VALUES (%s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (nickname,))
    cursor.close()
    user_id = get_user_id(nickname)

    query = "INSERT INTO attemps (start_date, timer, nb_ok, nb_total, game_id, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (start_date, duration, nbsuccess, nbtrials, idexercise, user_id))
    cursor.close()


def get_exercice_name(id):
    open_dbconnection()
    try:
        cursor = db_connection.cursor()
        query = "SELECT exercise FROM games WHERE exercise = %s"
        cursor.execute(query, (id, ))
        result = cursor.fetchone()
    except:
        result = query
    close_dbconnection()
    return result


def get_exercise_id(name):
    try:
        cursor = db_connection.cursor()
        query = "SELECT id FROM exercices WHERE name = %s"
        cursor.execute(query, (name, ))
        result = cursor.fetchone()[0]
    except:
        result = "Failed"
    return result


def infos_results(pseudo, exercise):
    open_dbconnection()
    infos = []
    cursor = db_connection.cursor()

    query = "SELECT users.nickname, start_date, timer, games.exercise, nb_ok, nb_total FROM attemps \
             INNER JOIN games ON attemps.game_id = games.id \
             INNER JOIN users ON attemps.user_id = users.id"

    if pseudo != "" and exercise != "":
        query += "WHERE users.nickname = %s AND exercise = %s"
        cursor.execute(query, (pseudo, exercise))
    elif pseudo != "":
        query += "WHERE users.nickname = %s"
        cursor.execute(query, pseudo)
    elif exercise != "":
        query += "WHERE games.exercise = %s"
        cursor.execute(query, exercise)
    else:
        cursor.execute(query)

    result = cursor.fetchall()
    infos.append(result)


    cursor.close()
    close_dbconnection()
    return infos


open_dbconnection()