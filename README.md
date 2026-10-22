# Cafe Management System

## Files
- `cafe_management.py` — Python Tkinter desktop application
- `cafe_management.sql` — Creates the MySQL database, tables, and sample data
- `requirements.txt` — Python dependency

## Setup on Windows

1. Install/start MySQL Server. MySQL Workbench is a client; the MySQL Server service must be running.
2. Open `cafe_management.sql` in MySQL Workbench and execute the full script (lightning bolt).
3. In `cafe_management.py`, set `DB_PASSWORD` to the password for your local MySQL `root` account. The current code uses `123456` as the initial example.
4. Open this extracted folder in VS Code.
5. In VS Code Terminal, run:
   ```bash
   python -m pip install -r requirements.txt
   python cafe_management.py
   ```

Default app login:
- Username: `admin`
- Password: `admin123`

Note: The app's login password is separate from your MySQL root password. Change `DB_PASSWORD` in the Python file to match your own MySQL setup.
