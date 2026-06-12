import os
import requests

def criar_tarefa_clickup(novo_cliente):
    CLICKUP_HEADER_AUTHORIZATION = os.getenv("clickup_header_authorization")
    CLICKUP_LIST_ID = os.getenv("clickup_list_id")
    CLICKUP_USER_ID = os.getenv("clickup_user_id")

    print(CLICKUP_HEADER_AUTHORIZATION)
    print(CLICKUP_LIST_ID)
    print(CLICKUP_USER_ID)

    create_task_url = f"https://api.clickup.com/api/v2/list/{CLICKUP_LIST_ID}/task"

    payload = {
        "name": novo_cliente.nome,
        "assignees": [int(CLICKUP_USER_ID)],
        "description": str(novo_cliente)
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": CLICKUP_HEADER_AUTHORIZATION
    }

    print("Enviando requisição para ClickUp...")

    response = requests.post(create_task_url, json=payload, headers=headers)

    print(response.text)
    return response