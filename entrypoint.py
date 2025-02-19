import os
import time
import socket
import subprocess

# Configurações do banco de dados
DATABASE = os.getenv("DATABASE", "postgres")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))

# Esperar pelo PostgreSQL
if DATABASE == "postgres":
    print("Esperando pelo PostgreSQL...")
    while True:
        try:
            with socket.create_connection((DATABASE_HOST, DATABASE_PORT), timeout=1):
                print("PostgreSQL está disponível")
                break
        except (OSError, ConnectionRefusedError):
            time.sleep(0.1)

# Aplicar migrações do banco de dados
print("Aplicando migrações...")
subprocess.run(["python", "manage.py", "migrate", "--no-input"], check=True)

# Coletar arquivos estáticos
print("Coletando arquivos estáticos...")
subprocess.run(["python", "manage.py", "collectstatic", "--no-input"], check=True)

# Iniciar o servidor
if __name__ == "__main__":
    import sys
    subprocess.run(sys.argv[1:], check=True)
