# 🛒 E-commerce Analytics: Modern Data Stack (Em Construção 🚧)

Este repositório contém um projeto prático de Engenharia de Dados e Analytics Engineering focado no setor de varejo/e-commerce. O objetivo é construir uma plataforma de dados ponta a ponta utilizando exclusivamente ferramentas **Open Source**, aplicando as melhores práticas do *Modern Data Stack (MDS)*.

## 🎯 Objetivo de Negócio
Simular o ambiente de dados de um e-commerce para centralizar informações transacionais isoladas, permitindo responder a perguntas críticas de negócio, como:
- Comportamento de compras e análise de RFM (Recência, Frequência, Valor Monetário).
- Performance logística e tempo de entrega.
- Análise de produtos e vendas.

**Fonte de Dados:** Dataset público da Olist (Kaggle).

## 🏗️ Arquitetura e Tech Stack
O projeto simula a separação física entre sistemas operacionais e analíticos, tudo orquestrado via containers:

- **Infraestrutura:** Docker & Docker Compose
- **Linguagem:** Python 3.12 (gerenciado via `pyenv` e `poetry`)
- **Bancos de Dados:** PostgreSQL (2 containers separados para OLTP e OLAP)
- **Ingestão (Extract & Load):** Scripts customizados em Python (`pandas`, `sqlalchemy`) utilizando processamento em *chunks* para eficiência de memória.
- **Transformação (Transform):** `dbt Core` (Arquitetura Medalhão: Bronze, Prata, Ouro) - *Em andamento*
- **Visualização de Banco:** pgAdmin4

## 🚀 Status do Projeto

- [x] **Configuração de Ambiente Segura:** Criação de variáveis de ambiente (`.env`) e `.gitignore` garantindo protocolo *Zero Credential Exposure*.
- [x] **Infraestrutura em Containers:** Spin-up do banco transacional (OLTP), Data Warehouse (OLAP) e pgAdmin.
- [x] **Seed Inicial (Simulação do Sistema):** Carga dos arquivos CSV para o PostgreSQL OLTP.
- [x] **Pipeline EL (Extract & Load):** Extração de dados do OLTP e ingestão no schema `raw` do OLAP, com otimização de RAM (streaming por lotes).
- [ ] **Integração dbt:** Inicialização do dbt Core com profiles baseados em variáveis de ambiente.
- [ ] **Modelagem Bronze/Prata:** Limpeza, padronização e cruzamento de entidades.
- [ ] **Modelagem Ouro:** Construção das tabelas Fato e Dimensão prontas para o BI.
- [ ] **Orquestração e Dashboard:** (Próximos passos).

## 💻 Como rodar (Até o momento)

1. Clone o repositório.
2. Crie um arquivo `.env` na raiz do projeto com as credenciais (veja `docker-compose.yml` para as chaves necessárias).
3. Suba a infraestrutura:
   ```bash
   docker compose up -d
   ```
4.Instale as dependências:
   ```bash
   poetry install
   ```
5.Execute a carga inicial (OLTP) e o pipeline de ingestão (OLAP):
   ```bash
   poetry run python src/load_olist_data.py
   poetry run python src/el_pipeline.py
   ```