import mysql.connector

conexao = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='cayque',
    password='123',
    database='bdDoCayque'
)
# connect literalmente representa uma conexão com 
# o banco de dados mysql. Para ter essa conexão
# é preciso passar o host, a porta, o usuário e a senha

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Banana (nome VARCHAR(50))")
cursor.execute("INSERT INTO Banana (nome) VALUES ('cayque2')")
cursor.execute("SELECT nome FROM Banana")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.commit()
conexao.close()
