import mysql.connector
from mysql.connector import Error


def userTable(id, username, usernum, lottnum, winmatch):
    connection = {
        'host': 'localhost',
        'username': 'root',
        'password': '',
        'database':'Lottery_results'
    }
    try:
        db = mysql.connector.connect (**connection)
        if db.is_connected ():
            print ("Successfully connected ")
            cursor = db.cursor ()
            # lottery_db = cursor.execute ("CREATE DATABASE Lottery_results")
            # lottery_result = cursor.execute("CREATE TABLE Play_History (userID INT, userName VARCHAR(50),userNumbers VARCHAR(50),lottNumbers VARCHAR(50),winMatches VARCHAR(50))")
            student_marks = "INSERT INTO Play_History(userID, userName,userNumbers,lottNumbers,winMatches) VALUES (%s,%s,%s,%s,%s)"
            data_table =(id,username,usernum,lottnum,(winmatch + " rounds win"))
            cursor.execute(student_marks,data_table)


            db.commit()
    except Error as e:
        print("Something is wrong -", e)

def userCheck():
    connection = {
        'host': 'localhost',
        'username': 'root',
        'password': '',
        'database':'Lottery_results'
    }

    new_db = mysql.connector.connect(**connection)
    try:
        if new_db.is_connected():
            new_cursor = new_db.cursor()
            user_check = str(input("Enter name :")).capitalize()
            new_cursor.execute("SELECT * FROM Play_History WHERE userName = %s", (user_check,))
            user_result = new_cursor.fetchall()
            if user_result:
                pass
            else:
                print(user_check, "is not in DB")
            for item in user_result:
                print(item)
    except Error as e:
        print("Something is wrong", e)


def html_view():
    import pandas, webbrowser
    connection = {
        'host': 'localhost',
        'username': 'root',
        'password': '',
        'database':'Lottery_results'
    }
    try:
        html_db = mysql.connector.connect(**connection)
        if html_db.is_connected():
            print("Successfully accessed!")
            fo = open('lottery_history.html', "w")
            sql_command = "SELECT * FROM Play_History"
            show = pandas.read_sql(sql_command, html_db)
            view = show.to_html()
            fo.write(view)

            webbrowser.open('lottery_history.html')



    except Error as  e:
        print("Something is wrong --- >",e)



# new_cursor.execute("SELECT * FROM Play_History WHERE userName ="+ user_check + ""    )