import sqlite3

DB = None
CONN = None


def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
title: %s
description: %s
max_grade: %d""" %(row[0], row[1], row[2])

def make_new_project(title, description, max_grade):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project, %s, which was to: %s, and is worth %s points." % (title, description, max_grade)

def get_grade_by_project(project_title):
    query = """SELECT student_github, project_title, grade  FROM Grades where project_title = ?"""
    DB.execute(query, (project_title,))
    row = DB.fetchone()
    print """\
    Project_title: %s
    Grade: %s""" %(row[2], row[3])

def make_new_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?,?,?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully updated %s's %s grade to %s." %(student_github, project_title, grade)


def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        if command == "new_student" or command == "new_grade":
            tokens = input_string.split()
        elif command == "new_project":
            tokens = input_string.split(", ")
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)

        if command == "project":
            get_project_by_title(*args)
        elif command == "new_project":
            make_new_project(*args)

        if command == "grade":
            get_grade_by_project(*args)
        elif command == "new_grade":
            make_new_grade(*args)

    CONN.close()

if __name__ == "__main__":
    main()
