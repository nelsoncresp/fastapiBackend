import mysql.connector

#configurar conex
mysql_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'BD_PAGINA_WEB',
    'auth_plugin': 'mysql_native_password'
}

connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection