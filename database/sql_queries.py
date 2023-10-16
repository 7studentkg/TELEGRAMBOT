CREATE_USER_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS telegram_users (
    ID INTEGER PRIMERY KEY,
    TELEGRAM_ID INTEGER,
    USERNAME CHAR(50),
    FIRST_NAME CHAR(50),
    LAST_NAME CHAR(50),
    UNIQUE (TELEGRAM_ID)
    )
'''

INSERT_USERS_QUERY = '''
    INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)

'''

SELECT_ALL_USERS_QUERY ='''
    SELECT * FROM telegram_users
'''

SELECT_USERS_QUERY ='''
    SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
'''

CREATE_BAN_USERS_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS ban_users (
    ID INTEGER PRIMERY KEY,
    TELEGRAM_ID INTEGER,
    USERNAME CHAR(50),
    COUNT INTEGER,
    UNIQUE (TELEGRAM_ID)
    )
'''

INSERT_BAN_USERS_QUERY = '''
    INSERT INTO ban_users VALUES (?,?,?,?)

'''

UPDATE_BAN_USERS_COUNT_QUERY = '''
    UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?

'''
