from database import session
from models.cliente_model import Cliente

class ClienteRepository:
    """Repositório para operações com clientes"""
    
    @staticmethod
    def criar(cliente: Cliente) -> Cliente:
        """Criar um novo cliente"""
        try:
            db = session()
            novo_cliente = Cliente(
                nome=cliente.nome,
                telefone=cliente.telefone,
                email=cliente.email,
                especialidade=cliente.especialidade,
                principal_desafio=cliente.principal_desafio
            )
            db.add(novo_cliente)
            db.commit()
            db.refresh(novo_cliente)
            return novo_cliente
        finally:
            db.close()