from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "TU_CONTRASEÑA_AQUÍ"  # Reemplaza con tu contraseña de pgAdmin
DB_PORT = "5432"

@app.route('/')
def inicio():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM libros;')
        total_libros = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return f"¡Conexión exitosa a PostgreSQL! Libros registrados: {total_libros}"
    except Exception as e:
        return f"Error exacto de conexión: {e}"

if __name__ == '__main__':
    app.run(debug=True)