import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='cayque',
    password='cayque321',
    database='cayqueDB2'
)

print(conexao)