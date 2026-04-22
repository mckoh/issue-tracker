"""
Issue Tracker App Code File
Author: Michael Kohlegger
Date: April 2026
"""

from sqlite3 import connect


def initialize_database(name="issue_tracker.db"):
    connection = connect(name)
    cursor = connection.execute("""
    create table if not exists issue (
        issue_id integer primary key autoincrement,
        name text,
        priority text,
        deadline datetime,
        is_done bool,
        description text
    );
    """)
    connection.commit()
    cursor.close()
    connection.close()

def add_issue(name, description, deadline):
    connection = connect("issue_tracker.db")
    sql = f"insert into issue (name, description, deadline, is_done) values ('{name}', '{description}', '{deadline}', 0);"
    cursor = connection.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

def get_issues():
    connection = connect("issue_tracker.db")
    sql = "SELECT * FROM issue WHERE is_done = 0;"
    cursor = connection.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def set_issue_to_done(issue_id):
    connection = connect("issue_tracker.db")
    sql = f"UPDATE issue SET is_done = 1 WHERE issue_id = {issue_id};"
    cursor = connection.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

