from flask import Flask, request, jsonify
from schemas.cliente_schema import Cliente
from database import engine, Base
from repositories.cliente_repository import ClienteRepository
from clickup import criar_tarefa_clickup

app = Flask(__name__)

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

@app.route('/api/v1/cliente', methods=['POST'])
def create_client():
    """
    Criar um novo cliente no banco de dados
    """
    try:
        dados = request.get_json()

        if not dados:
            return jsonify({
                "erro": "JSON não informado"
            }), 400

        # Validar dados com Pydantic
        cliente_validado = Cliente.model_validate(dados)
        novo_cliente = ClienteRepository.criar(cliente_validado)
        response = criar_tarefa_clickup(novo_cliente)        

        return jsonify({
            "mensagem": "Cliente criado com sucesso",
            "cliente_id": novo_cliente.id,
            "clickup_response": response.json()
        }), 201

    except ValueError as e:
        return jsonify({
            "erro": str(e)
        }), 400

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)