from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime, timezone

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)

    nome = Column(String)
    telefone = Column(String)
    email = Column(String, unique=True)
    especialidade = Column(String)
    principal_desafio = Column(String)

    criado_em = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEspecialidade: {self.especialidade}\nPrincipal Desafio: {self.principal_desafio}"