# 🛒 E-commerce Analytics: Modern Data Stack (Em Construção 🚧)

Este repositório contém um projeto prático de Engenharia de Dados e Analytics Engineering focado no setor de varejo/e-commerce. O objetivo é construir uma plataforma de dados de ponta a ponta utilizando exclusivamente ferramentas **Open Source**, aplicando as melhores práticas do *Modern Data Stack (MDS)*.

## 🎯 Objetivo de Negócio
Simular o ambiente de dados de um e-commerce para centralizar informações transacionais isoladas, permitindo responder a perguntas críticas de negócio, como:
- Comportamento de compras e análise de RFM (Recência, Frequência, Valor Monetário).
- Performance logística e tempo de entrega.
- Análise de produtos e vendas por região.

**Fonte de Dados:** Dataset público da Olist (Kaggle).

## 🏗️ Arquitetura e Tech Stack
O projeto simula a separação física entre sistemas operacionais e analíticos, tudo orquestrado via containers:

- **Infraestrutura:** Docker & Docker Compose
- **Linguagem:** Python 3.12 (gerenciado via `pyenv` e `poetry`)
- **Bancos de Dados:** PostgreSQL (2 containers separados para OLTP e OLAP)
- **Ingestão (Extract & Load):** Scripts customizados em Python (`pandas`, `sqlalchemy`) utilizando processamento em *chunks* para eficiência de memória.
- **Transformação (Transform):** `dbt Core` (Arquitetura Medalhão: Bronze, Prata, Ouro)
- **Visualização de Dados:** `Streamlit` e `Plotly` (Dashboard interativo em Python puro)
- **Gestão de Base de Dados:** pgAdmin4

## 🚀 Status do Projeto

- [x] **Configuração de Ambiente Segura:** Criação de variáveis de ambiente (`.env`) e `.gitignore` garantindo protocolo *Zero Credential Exposure*.
- [x] **Infraestrutura em Containers:** Spin-up do banco transacional (OLTP), Data Warehouse (OLAP) e pgAdmin.
- [x] **Seed Inicial (Simulação do Sistema):** Carga dos arquivos CSV para o PostgreSQL OLTP.
- [x] **Pipeline EL (Extract & Load):** Extração de dados do OLTP e ingestão no schema `raw` do OLAP, com otimização de RAM (streaming por lotes).
- [x] **Integração dbt:** Inicialização do dbt Core com profiles baseados em variáveis de ambiente.
- [x] **Modelagem Bronze/Prata:** Limpeza, padronização e cruzamento de entidades (`stg_customers`, `stg_orders`).
- [x] **Modelagem Ouro:** Construção da tabela Fato para BI (`fct_customer_orders`).
- [x] **Qualidade de Dados:** Implementação de testes automatizados no dbt (schema tests).
- [x] **Catálogo e Linhagem (Lineage):** Geração de documentação interativa via `dbt docs`.
- [x] **Visualização (Dashboard):** Construção de um painel analítico interativo consumindo a camada Ouro com Streamlit.
- [ ] **Orquestração:** (Próximos passos para automação do pipeline).

## 💻 Como rodar (Até o momento)

1. Clone o repositório.
2. Crie um arquivo `.env` na raiz do projeto com as credenciais (veja `docker-compose.yml` para as chaves necessárias).
3. Suba a infraestrutura:
   ```bash
   docker compose up -d
   ```
4. Instale as dependências:
   ```bash
   poetry install
   ```
5. Execute a carga inicial (OLTP) e o pipeline de ingestão (OLAP):
   ```bash
   poetry run python src/load_olist_data.py
   poetry run python src/el_pipeline.py
   ```
6. Execute as transformações do dbt:
   ```bash
   # Carregue as variáveis de ambiente e rode o dbt
   export $(cat .env | xargs)
   cd ecommerce_analytics
   poetry run dbt run
   ```
   # Valide a qualidade dos dados
   ```
   poetry run dbt test
   ```

7. Gere a documentação do dbt:
   ```
   poetry run dbt docs generate
   poetry run dbt docs serve
   ```
   # Acesse http://localhost:8080 no seu navegador

8. Execute o dashboard:
   # Volte para a raiz do projeto e carregue as variáveis
   ```bash
   cd ..
   export $(cat .env | xargs)
   poetry run streamlit run src/dashboard.py
   ```
# O painel abrirá automaticamente no seu navegador

