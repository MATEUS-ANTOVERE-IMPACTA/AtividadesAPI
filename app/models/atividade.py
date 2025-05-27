from app import db
import requests

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "professor_id": self.professor_id
        }

    @staticmethod
    def criar(data):
        campos = ['titulo', 'descricao', 'professor_id']
        for campo in campos:
            if campo not in data:
                return {"erro": f"Campo ausente: {campo}"}, 400

        # Verificação se o professor existe na DEVAPI
        try:
            r = requests.get(f"http://localhost:5000/professores/{data['professor_id']}")
            if r.status_code != 200:
                return {"erro": "Professor não encontrado na DEVAPI"}, 400
        except requests.exceptions.ConnectionError:
            return {"erro": "Erro ao conectar com o DEVAPI"}, 500

        atividade = Atividade(**data)
        db.session.add(atividade)
        db.session.commit()
        return atividade.to_dict(), 201