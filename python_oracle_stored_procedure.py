import cx_Oracle

# Informações de conexão
username = 'TESTE'
password = 'TESTE'
host = 'localhost'  # Endereço do servidor
port = 1521        # Número da porta padrão do Oracle
service_name = 'XEPDB1'

# String de conexão
dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

# Conectar-se ao banco de dados
connection = cx_Oracle.connect(username, password, dsn)

# Criar um cursor
cursor = connection.cursor()

# Consulta SQL
sql = 'SELECT * FROM tb_plataformas'

# Executar a consulta
cursor.execute(sql)

# Recuperar os resultados
for row in cursor:
    print(f'Id: {row[0]}, Plataforma: {row[1]}')

numero_plataformas = cursor.var(int)

# Retornando o número total de plataformas através de uma stored procedure em PL/SQL no Oracle com envio de parâmetro.
cursor.callproc('PKG_PLATAFORMA.SP_TOTAL_PLATAFORMAS', ['', numero_plataformas])
print(numero_plataformas.getvalue())

# Fechar o cursor
cursor.close()

