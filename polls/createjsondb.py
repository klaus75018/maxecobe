import sqlite3
import json

DB = "./db.sqlite3"

def get_all_users( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT * from PricingDBSite
    ''').fetchall()

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON

    return rows