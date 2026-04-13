# bootcamp-dieta-
Aplicação para ajudar a monitorar a dieta.

Davi Souza - Ra:22503048

# 🥗 App de Dieta - Registro Diário

Um aplicativo web simples e direto, construído com Python e Django, focado em ajudar o usuário a registrar e acompanhar seu peso e a ingestão diária de calorias. 

Este projeto foi desenvolvido como um MVP (Produto Mínimo Viável) para consolidar conceitos básicos de back-end, banco de dados e autenticação com Django.

---

## ✨ Funcionalidades

* **Sistema de Autenticação:** Login e logout utilizando o sistema nativo e seguro do Django.
* **Privacidade de Dados:** Cada usuário tem acesso exclusivo apenas aos seus próprios registros.
* **Registro de Peso:** Inserção do peso atual com registro automático da data.
* **Registro de Alimentos:** Anotação de refeições e quantidade de calorias consumidas no dia.
* **Dashboard / Histórico:** Uma tela principal que lista, de forma cronológica, todo o histórico de pesos e alimentos registrados.
* **Painel Administrativo:** Acesso completo aos dados via `/admin` do Django para superusuários.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Django
* **Banco de Dados:** SQLite (padrão do Django)
* **Front-end:** HTML5 e CSS3 (renderizado via Django Templates)

---

## 🚀 Como executar o projeto localmente

Siga o passo a passo abaixo para rodar o aplicativo na sua máquina.

### 1. Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.

### 2. Clone o repositório e acesse a pasta
Se você ainda não baixou o projeto, clone-o através do Git e entre na pasta raiz:
```bash
git clone https://github.com/davi-ssg/bootcamp-dieta-.git
cd nome-da-pasta-do-projeto