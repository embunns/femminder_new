import sqlite3

conn = sqlite3.connect('users.db')  # Ganti dengan nama database Anda
cursor = conn.cursor()

# Query untuk menampilkan struktur tabel
cursor.execute("PRAGMA table_info(user)")

# Tampilkan struktur tabel
columns = cursor.fetchall()
for column in columns:
    print(column)

conn.close()
