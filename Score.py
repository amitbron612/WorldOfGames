import mysql.connector
POINTS_OF_WINNING = 5


def add_score(name, difficulty):
    points = (difficulty * 3) + POINTS_OF_WINNING

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
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
    db.close()
