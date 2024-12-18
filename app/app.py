from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuration pour la base de données PostgreSQL
DATABASE = {
    'dbname': 'integration_db',
    'user': 'integration_user',
    'password': 'secure_password',
    'host': 'db',
    'port': 5432
}

def connect_db():
    return psycopg2.connect(**DATABASE)

@app.route('/')
def index():
    return "Bienvenue sur la Plateforme d'Intégration Communautaire"

@app.route('/api/places', methods=['GET'])
def get_places():
    # Exemple de réponse
    return jsonify({"message": "Liste des lieux géolocalisés"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')