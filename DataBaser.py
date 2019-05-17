import sqlite3

# conectando...
conn = sqlite3.connect('Remedios.db')
# definindo um cursor
cursor = conn.cursor()



# criando a tabela (schema)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Remedios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Preco TEXT NOT NULL,
        Categoria TEXT,
        QuantidadeRemedio TEXT NOT NULL,
        Horario TEXT NOT NULL,
        QuantidadeUso TEXT NOT NULL,
        Receita TEXT NOT NULL
        

);
""")

print('Tabela criada com sucesso.')
# desconectando...



'''
# inserindo dados na tabela
cursor.execute("""
INSERT INTO Remedios (nome, preco)
VALUES ('Dipirona', '2,50')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')
'''
