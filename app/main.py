from app import create_app
from app.extensions import db
from app.models.atividade import Atividade

app = create_app()

with app.app_context():
    db.create_all()  # Cria as tabelas se não existirem

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)