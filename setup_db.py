import sqlite3

conn = sqlite3.connect('threat_intel.db')
cursor = conn.cursor()

# Create a table for Indicators of Compromise (IoCs)
cursor.execute('''CREATE TABLE IF NOT EXISTS iocs (indicator TEXT, type TEXT)''')

# Insert the blocked processes from your Atomic Red Team test
cursor.execute("INSERT INTO iocs VALUES ('rdrleakdiag.exe', 'Suspicious Process')")
cursor.execute("INSERT INTO iocs VALUES ('xordump.exe', 'Suspicious Process')")
cursor.execute("INSERT INTO iocs VALUES ('Invoke-AtomicTest', 'Red Team Framework')")

conn.commit()
conn.close()
print("Threat Intel Database created successfully.")