# Desafio Técnico - Brio Lab

Este repositório contém a implementação dos dois desafios propostos pela Brio Lab para a vaga de Desenvolvedor(a) de Automação & IA.

# 🛠️ Desafio 1 - Orquestração com n8n

<p align="center">
  <img src="https://img.shields.io/badge/n8n-FF6C37?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n">
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase">
  <img src="https://img.shields.io/badge/ClickUp-7B68EE?style=for-the-badge&logo=clickup&logoColor=white" alt="ClickUp">
  <img src="https://img.shields.io/badge/Gemini-8E75FF?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
</p>

## Objetivo
Desenvolver um fluxo de automação utilizando [n8n](https://n8n.io/) para monitorar tarefas aprovadas no [ClickUp](https://clickup.com), processar automaticamente suas legendas com Inteligência Artificial para geração de hashtags, armazenar os resultados em um banco de dados e notificar o responsável pela publicação, eliminando etapas manuais do processo.

## Fluxo
| Etapa | Descrição |
| :--- | :--- |
| **ClickUp Trigger** | Monitora alterações em tempo real nas tarefas do ClickUp |
| **Filtro de Status** | Processa apenas tarefas com status Aprovada |
| **Obtenção da Tarefa** | Recupera os dados completos da tarefa via API do ClickUp |
| **Tratamento dos Dados** | Extrai e organiza os campos necessários para o processamento |
| **Geração de Hashtags com IA** | Utiliza o [Google Gemini](https://ai.google.dev/) para gerar hashtags com base na legenda |
| **Structured Output Parser** | Padroniza o retorno da IA em formato estruturado |
| **Persistência dos Dados** | Salva os resultados processados no [Supabase](https://supabase.com/) |
| **Notificação** | Envia um e-mail com a confirmação do processamento |

## Demonstração do Fluxo no n8n
<img width="800" height="336" alt="Execução" src="https://github.com/user-attachments/assets/5bfeddfc-0345-4c39-bf69-1e8b35f7d1b5" />

# 🛠️ Desafio 2 - Backend com Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase">
  <img src="https://img.shields.io/badge/ClickUp-7B68EE?style=for-the-badge&logo=clickup&logoColor=white" alt="ClickUp">
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman">
</p>

## Objetivo
Desenvolver uma API em Python capaz de receber dados de um formulário de diagnóstico, validar e normalizar as informações recebidas, armazená-las em banco de dados e integrar-se à API do ClickUp para criar automaticamente uma tarefa na lista de leads, atribuindo-a a um responsável.

Para aproximar a solução de um cenário real de produção, foi utilizado o Supabase como banco de dados para persistência das informações processadas.

## Estrutura do Projeto

A arquitetura do projeto foi desenhada seguindo o padrão de separação de responsabilidades (Repository Pattern / Camadas):

```text
second-challenge/
├── models/
│   └── cliente_model.py     
├── repositories/
│   └── cliente_repository.py  
├── schemas/
│   └── cliente_schema.py    
├── tests/
│   └── Brio - Lab.postman_collection.json  
├── .env.example               
├── app.py                     
├── clickup.py                
├── database.py                
├── requirements.txt          
└── utils.py           
```
## Tecnologias Utilizadas

* **Linguagem Principal:** [Python](https://www.python.org/)
* **Framework Web:** [Flask](https://flask.palletsprojects.com/)
* **Banco de Dados:** [Supabase (PostgreSQL)](https://supabase.com/)
* **Integrações:** [ClickUp API](https://clickup.com/api/)
* **Validação & Ferramentas:** [Postman](https://www.postman.com/)

## Como Configurar e Executar
### Pré-requisitos
- Python 3.11 ou superior instalado.

### Instalação e Ambiente Virtual
```bash
git clone <url-do-seu-repositorio>
cd second-challenge
```
### Crie e ative o ambiente virtual (.venv):
``` bash
# Criar ambiente
python -m venv .venv

# Ativar no Linux/macOS
source .venv/bin/activate

# Ativar no Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```
### Instale as dependências necessárias:
``` bash
pip install -r requirements.txt
```
### Configuração de Variáveis de Ambiente:
``` bash
cp .env.example .env
```
### Execução do Servidor
``` bash
python app.py
```
**A API estará disponível localmente em:** http://localhost:5000

## ✅ Casos de Teste Executados
**Cenários de Sucesso**
- Cadastro de cliente válido.
  
**Cenários de Erro**
- Requisição sem corpo JSON;
- E-mail inválido;
- Telefone inválido;
- Campo obrigatório ausente.

## 📝 Decisões Técnicas
### Utilização do Supabase
Embora o desafio permitisse a utilização de SQLite, foi escolhido o Supabase por oferecer uma experiência mais próxima de um ambiente real de produção, além de facilitar futuras integrações e escalabilidade da solução.

### Integração com ClickUp
Foi implementada a criação automática de tarefas por meio da API do ClickUp, permitindo que cada lead recebido seja encaminhado diretamente para o fluxo operacional. 

Também foi adicionada a atribuição automática da tarefa a um responsável.

### Validação dos Dados
A validação foi centralizada utilizando Pydantic, garantindo consistência das informações antes de qualquer processamento ou persistência.

## 👨‍💻 Melhorias Futuras
Com mais tempo de desenvolvimento, poderiam ser implementadas as seguintes melhorias:
- Testes automatizados;
- Logs estruturados;
- Documentação automática da API;
- Autenticação JWT para proteção dos endpoints;
