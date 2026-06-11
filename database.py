```python
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Reviews Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    code TEXT NOT NULL,
    result TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")
```

```
```
