# Desafio Técnico - Brio Lab

Este repositório contém a implementação dos dois desafios propostos pela Brio Lab para a vaga de Desenvolvedor(a) de Automação & IA.

# 🛠️ Desafio 1 - Orquestração com n8n

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

# Desafio 2 - Backend com Python

## Objetivo
Simular o recebimento de um JSON com campos de diagnósico (nome, telefone, e-mail, especialidade, principal desafio). Validar os campos obrigatórios, formatar telefone, normalizar e-mail. Conectar a um banco de dados (foi utilizado o Supabase para aproximar do ambiente real) e inserir os dados tratados. Utilizar uma API do clickup para criar uma tarefa na lista de leads com os dados do formulário, marcando um responsável.
