import mysql.connector

POINTS_OF_WINNING = 5

def add_score(name, difficulty):
    points = (difficulty * 3) + POINTS_OF_WINNING

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="games"
    )
    cursor = db.cursor()

    # Insert or update the score in the users_scores table
    query = "INSERT INTO users_scores (name, score) VALUES (%s, %s) ON DUPLICATE KEY UPDATE score = score + %s"
    cursor.execute(query, (name, points, points))

    # Commit the transaction and close the connection
    db.commit()
    cursor.close()
    db.close()

def get_all_scores():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="games"
    )
    cursor = db.cursor()

    # Retrieve all scores sorted by score in descending order
    query = "SELECT name, score FROM users_scores ORDER BY score DESC"
    cursor.execute(query)
    scores = cursor.fetchall()

    # Close the connection
    cursor.close()
    db.close()

    return scores
