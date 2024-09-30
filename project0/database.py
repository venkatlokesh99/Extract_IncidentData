import sqlite3

def connectdb():
    db = sqlite3.connect('resources/normanpd.db')
    cursor = db.cursor()

    return (cursor,db)

def createdb():
    """
    Creates an SQLite database and returns the connection object.
    """
    (cur,db) = connectdb()
    # Create the incidents table
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
        incident_time TEXT,
        incident_number TEXT,
        incident_location TEXT,
        nature TEXT,
        incident_ori TEXT
    )''')
    db.commit()

def populatedb(incidents):
    """
    Inserts the incidents into the database.
    """
    (cur,db) = connectdb()
    for incident in incidents:
        cur.execute('''INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)
                          VALUES (?, ?, ?, ?, ?)''', 
                          (incident["DateTime"], incident["IncidentNumber"], 
                           incident["Location"], incident["Nature"], 
                           incident["IncidentType"]))
    db.commit()

def status():
    """
    Prints a summary of the incidents.
    Output the nature of incidents and the number of times they have occurred.
    """
    (cur,db) = connectdb()
    
    cur.execute('''SELECT nature, COUNT(*) as count FROM incidents 
                      GROUP BY nature ORDER BY nature ASC''')
    
    for row in cur.fetchall():
        print(f'{row[0]}|{row[1]}')
    
    db.close()
    
def deletedb():
    """
    Deletes existing Table from the DB to prevent duplication of data
    """
    (cur,conn) = connectdb()
    
    cur.execute('''DROP TABLE IF EXISTS incidents''')