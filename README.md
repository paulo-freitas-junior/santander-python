# santander-python

Curso Python do Santander — repositório de estudos com exemplos práticos das aulas.
---
[![Status](https://img.shields.io/badge/status-Concluído-green)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO)
[![Licença](https://img.shields.io/badge/licença-MIT-blue)](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/blob/main/LICENSE)

---
## Sobre

Este repositório reúne os scripts desenvolvidos durante o curso de Python oferecido pelo Santander. Os exemplos estão organizados em ordem crescente de complexidade, cobrindo desde o primeiro programa ("Olá Mundo") até tópicos como tratamento de erros, entrada e saída de dados, módulos e pacotes.

O conteúdo é destinado a fins educacionais e de aprendizado da linguagem Python.

## Estrutura do projeto

```text
santander-python/
├── data/
│   └── dados.txt                       # Arquivo de exemplo para leitura/escrita
├── src/
│   ├── 01-script_inicial.py            # Primeiro programa em Python (print)
│   ├── 02-tipos_dados.py               # Tipos de dados: int, float, str, bool
│   ├── 03-variaveis.py                 # Declaração e uso de variáveis
│   ├── 04-operadores.py                # Operadores aritméticos, de comparação e lógicos
│   ├── 05-estruturas_condicionais.py   # if, elif, else
│   ├── 06-loops.py                     # Laços de repetição for e while
│   ├── 07-listas.py                    # Listas: criação, indexação e métodos
│   ├── 08-tuplas.py                    # Tuplas imutáveis
│   ├── 09-dicionarios.py               # Dicionários: chave-valor
│   ├── 10-conjuntos.py                 # Conjuntos (sets)
│   ├── 11-funcoes.py                   # Funções, parâmetros, return, lambda, escopo, docstrings
│   ├── 12-tratamentoErros.py           # Tratamento de erros
│   ├── 13-excecoes.py                  # Exceções
│   ├── 14-entradas_saidas.py           # Entrada e saída de dados (input/print)
│   ├── 15-leitura_escrita.py           # Leitura e gravação de arquivos
│   ├── 16-importacao_modulos.py        # Importação de módulos (math, random, datetime)
│   ├── 17-modulo_personalizado.py      # Criação e uso de módulos próprios
│   ├── 18-pacotes.py                   # Organização em pacotes
│   ├── meu_modulo_exemplo.py           # Módulo de exemplo (saudar, calcular_soma)
│   ├── operacoes.py                    # Módulo de operações matemáticas básicas
│   └── utilidades.py                   # Módulo de utilidades para interação com usuário
├── .gitignore                          # Ignorados do Git (Python)
├── LICENSE                             # Licença MIT
└── README.md                           # Este arquivo
```

## Tópicos abordados

1. Primeiros passos com Python
2. Tipos de dados primitivos
3. Variáveis
4. Operadores
5. Estruturas condicionais
6. Laços de repetição
7. Listas
8. Tuplas
9. Dicionários
10. Conjuntos
11. Funções (incluindo lambdas, escopo e docstrings)
12. Tratamento de erros
13. Exceções
14. Entrada e saída de dados
15. Leitura e escrita de arquivos
16. Importação de módulos padrão
17. Módulos personalizados
18. Pacotes

## Como executar

Pré-requisitos: Python 3 instalado.

Execute qualquer script da pasta `src/` diretamente:

```bash
python src/01-script_inicial.py
```

Para scripts que leem arquivos da pasta `data/`, execute a partir da raiz do repositório:

```bash
python src/15-leitura_escrita.py
```

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
