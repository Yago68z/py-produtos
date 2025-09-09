from db  import db 

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key =True)
    modelo = db.Column(db.String(80), nullable = False)
    marca = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.Interger, nullable=False)
    
    def json(self):
        return {
            'id' : self.id,
            'modelo': self.modelo,
            'marca': self.marca,
            'ano' : self.ano
            
        }
    