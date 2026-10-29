
# 🏢 Auditoria de Orçamentos Corporativos (Python)

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque)
[![Projeto](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)](https://www.python.org/)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de Programação em Python do curso de Engenharia de Software. O objetivo é processar e calcular o orçamento de uma estrutura organizacional utilizando dicionários aninhados e recursos fundamentais da linguagem Python.

A solução simula a auditoria de recursos financeiros de uma empresa, permitindo percorrer diferentes níveis hierárquicos, desconsiderar departamentos específicos e converter o valor total para outra moeda conforme uma taxa de câmbio informada.

## 🚀 Funcionalidades

- 🏢 **Cálculo Hierárquico:** percorre a estrutura organizacional para calcular o orçamento total dos departamentos.
- 🔎 **Filtros Dinâmicos:** permite ignorar departamentos específicos durante o cálculo.
- 💱 **Conversão de Moeda:** possibilita converter o orçamento calculado utilizando uma taxa de câmbio.
- 🌳 **Estrutura Flexível:** trabalha com dicionários aninhados de diferentes níveis de profundidade.
- 📊 **Auditoria de Recursos:** organiza os valores financeiros para facilitar a análise do orçamento corporativo.

## 🛠️ Tecnologias e Conceitos Aplicados

O projeto utiliza Python e sua biblioteca padrão, sem a necessidade de instalar dependências externas.

- 🐍 **Python:** linguagem utilizada no desenvolvimento do sistema.
- 🔁 **Funções Recursivas:** percorrem estruturas hierárquicas de forma automática.
- 📦 **Dicionários Aninhados:** representam departamentos, setores e seus respectivos orçamentos.
- 🔧 **Parâmetros `*args`:** permitem receber departamentos que devem ser ignorados.
- ⚙️ **Parâmetros `**kwargs`:** possibilitam configurar opções adicionais, como moeda e taxa de câmbio.
- 🧮 **Operações Matemáticas:** realizam somas e conversões de valores financeiros.

## 🧠 Lógica de Funcionamento

O sistema utiliza uma função recursiva para analisar a estrutura corporativa.

1. **Leitura da estrutura:** recebe um dicionário com os departamentos e seus respectivos valores ou subdivisões.
2. **Verificação dos departamentos:** identifica quais departamentos devem participar do cálculo.
3. **Soma dos orçamentos:** percorre os níveis da estrutura e acumula os valores válidos.
4. **Aplicação de filtros:** ignora os departamentos especificados pelo usuário.
5. **Conversão de moeda:** aplica a taxa de câmbio configurada, quando solicitada.
6. **Exibição do resultado:** apresenta o orçamento calculado após as operações.

## ⚙️ Como Executar

### 📋 Pré-requisitos

- Python 3.8 ou superior instalado.
- Terminal ou editor de código, como Visual Studio Code.

### ▶️ Passo a Passo

**1. Clone o repositório**

```bash
git clone https://github.com/Lusca2803/projeto-sistema-de-auditoria-de-recursos-corporativos.git
```

**2. Acesse a pasta do projeto**

```bash
cd projeto-sistema-de-auditoria-de-recursos-corporativos
```

**3. Execute o programa**

```bash
python main.py
```

> 💡 Não são necessárias bibliotecas externas. O programa utiliza recursos nativos do Python.

## 📂 Estrutura do Projeto

```text
Sistemas_de_auditoria_de_recursos_corporativos/
├── README.md
└── main.py
```

- 📘 `README.md`: documentação e instruções para execução.
- 🐍 `main.py`: código principal responsável pelos cálculos recursivos e pela auditoria dos orçamentos.

## 💻 Acesse o Projeto

🐍 **[Visualizar código-fonte (main.py)](main.py)**

📁 **[Acessar repositório do projeto no GitHub](https://github.com/Lusca2803/projeto-sistema-de-auditoria-de-recursos-corporativos)**

📂 **[Acessar pasta do projeto no portfólio](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main/Sistemas_de_auditoria_de_recursos_corporativos)**

## 👤 Autor

**Matheus Chagas Mauriz Coque**

🎓 Estudante de Engenharia de Software

- 💼 [LinkedIn](https://www.linkedin.com/in/matheus-chagas-coque-b190ba39b/)
- 🐙 [GitHub](https://github.com/chagasmatheus1211)
- 📧 [E-mail](mailto:chagasmatheus1211@gmail.com)

---

⭐ *Projeto acadêmico com foco em recursão, estruturas de dados, filtros dinâmicos e cálculos de orçamento corporativo.*

⬅️ **[Voltar ao portfólio principal](https://github.com/chagasmatheus1211/portfolio-matheus-chagas-mauriz-coque/tree/main)**
