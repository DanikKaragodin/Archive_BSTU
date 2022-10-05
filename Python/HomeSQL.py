from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
        database = "online_movie_rating",
    ) as connection:
        print(connection)
        # create_db_query="CREATE DATABASE online_movie_rating"
        # show_db_query = "SHOW DATABASES"
        create_movies_table_query="""
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
        create_reviewers_table_query ="""
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""
        create_ratings_table_query ="""
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""
        with connection.cursor() as cursor:
            try:
                cursor.execute(create_movies_table_query)
            except Error as e:
                print(e)
            
            try:
                cursor.execute(create_ratings_table_query)
            except Error as e:
                print(e)

            try:
                cursor.execute(create_reviewers_table_query)
            except Error as e:
                print(e)
            connection.commit()
            

except Error as e:
    print(e)
