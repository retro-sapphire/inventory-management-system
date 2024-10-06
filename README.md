# Initial Configuration
You only need to do this once if you are working as a developer on the program.
This program is only supported on Windows.

Make sure you have the following installed:
- [Python 3.12](https://www.python.org/downloads/)
- [MySQL 8.4.0](https://dev.mysql.com/downloads/mysql/)
- [GIT](https://www.git-scm.com/download/)

Now do this before running the program:

0. Clone this GIT Repository
```bash
git clone https://github.com/grobo021/holiday-homework
```

1. Create a .venv environment
```bash
python3 -m venv .venv
```

2. Install necessary packages
```bash
pip install -r requirements.txt
```

3. Make a .env file and copy/paste the following. Make sure to change the data depending on the name of your database, and the password of the root user.
```env
DB_DOMAIN=localhost
DB_USER=root
DB_PASS=[PASSWORD]
DB_NAME=[DATABASE_NAME]
```

# Running the Program
When developing/testing, use this to run as a normal Python program

```bash
python3 init.py
```

# Setup for the sample database
Open the mysql command line and run the following command to quickly set up a sample database.

```mysql
source sample_db.sql;
```