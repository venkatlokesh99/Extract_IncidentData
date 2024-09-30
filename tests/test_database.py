import sqlite3
import os
from project0.database import createdb, populatedb, deletedb, status, connectdb


def test_connectdb():
    (cur,db) = connectdb()

    # Check if the database connection is an instance of sqlite3.Connection
    assert isinstance(db, sqlite3.Connection)

    # Check if the cursor is an instance of sqlite3.Cursor
    assert isinstance(cur, sqlite3.Cursor)

    # Ensure the database file is created
    assert os.path.exists('resources/normanpd.db')

    # Test if the cursor can execute a simple query
    cur.execute("SELECT 1")
    result = cur.fetchone()
    
    # Ensure the query result is correct
    assert result[0] == 1

    db.close()

def test_createdb():
    # Create the database and table
    deletedb()
    createdb()

    (cur,db) = connectdb()

    # Check if the table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents';")
    result = cur.fetchone()

    assert result is not None
    assert result[0] == 'incidents'

    db.close()

def test_populatedb():
    # Insert mock data into the database
    incidents = [{"DateTime": "9/23/2024 0:21", "IncidentNumber": "2024-00069441", "Location": "1251 ALAMEDA ST", "Nature": "Burglary", "IncidentType": "OK0140200"}]
    populatedb(incidents)

    (cur,db) = connectdb()

    # Check if data was inserted
    cur.execute("SELECT * FROM incidents")
    rows = cur.fetchall()

    assert len(rows) == 1
    assert rows[0][0] == '9/23/2024 0:21'
    assert rows[0][1] == '2024-00069441'

    db.close()


def test_status(capfd):

    incidents = [{"DateTime": "9/23/2024 1:45", "IncidentNumber": "2024-00069442", "Location": "525 ANOTHER ST", "Nature": "Theft", "IncidentType": "OK0140300"}]
    populatedb(incidents)

    # Check if status prints the correct summary
    status()
    captured = capfd.readouterr()

    assert "Burglary" in captured.out
    assert "Theft" in captured.out

def test_deletedb():
    # Delete the database table
    deletedb()

    (cur,db) = connectdb()

    # Check if the table was deleted
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='incidents';")
    result = cur.fetchone()

    assert result is None

    db.close()

