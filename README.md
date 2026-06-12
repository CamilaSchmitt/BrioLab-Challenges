# Desafio Técnico - Brio Lab

Este repositório contém a implementação dos dois desafios propostos pela Brio Lab para a vaga de Desenvolvedor(a) de Automação & IA.

# Desafio 1 - Orquestração com N8N

## Objetivo
Construir um fluxo automatizado capaz de detectar a aprovação de uma tarefa, processar sua legenda utilizando Inteligência Artificial, persistir os resultados em banco de dados e notificar o responsável pela publicação.

## Fluxo

### 1.ClickUp Trigger
- Monitora alterações nas tarefas do ClickUp;
- Sempre que uma tarefa é atualizada, o evento é enviado para o N8N.
### 2.Filtro de Status
- Verifica se a tarefa foi movida para o status "Aprovada";
- Garante que apenas conteúdos aprovados sejam processados.
### 3.Obtenção dos Dados da Tarefa
- Recupera as informações completas da tarefa aprovada através da API do ClickUp.
### 4.Tratamento dos Dados
- Extrai apenas os campos necessários para o processamento;
- Organiza os dados em uma estrutura padronizada para as próximas etapas.
### 5.Geração de Hashtags com IA
- Utiliza o Google Gemini para analisar a legenda da publicação;
- Gera hashtags relevantes para Instagram com base no conteúdo fornecido;
- Utiliza um Structured Output Parser para garantir um retorno estruturado e consistente.
### 6.Persistência dos Dados
- Armazena as informações processadas e as hashtags geradas em uma tabela no Supabase.
### 7.Notificação
- Envia uma notificação por e-mail utilizando o Gmail;
- Informa a conclusão do processamento e apresenta as hashtags sugeridas pela IA.


# Desafio 2 - Backend com Python

## Objetivo
Simular o recebimento de um JSON com campos de diagnósico (nome, telefone, e-mail, especialidade, principal desafio). Validar os campos obrigatórios, formatar telefone, normalizar e-mail. Conectar a um banco de dados (foi utilizado o Supabase para aproximar do ambiente real) e inserir os dados tratados. Utilizar uma API do clickup para criar uma tarefa na lista de leads com os dados do formulário, marcando um responsável.
