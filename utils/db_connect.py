import pyodbc


def connect():
    host = "localhost"
    user = "root"
    password = "root"
    database = "covid"
    driver = pyodbc.drivers()
    driver = list(filter(lambda d: 'MySQL' in d, driver))
    print(driver)
    conn_string = f'DRIVER={{{driver[0]}}};UID={user};Password={password};Server={host};Database={database};Port=3306'
    cnxn = pyodbc.connect(conn_string)
    return cnxn
