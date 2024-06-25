# Solucionador do Problema do Caixeiro Viajante

Este repositório contém uma implementação para resolver o Problema do Caixeiro Viajante (TSP) usando três algoritmos diferentes: Hill Climbing, Algoritmo Genético e Têmpera Simulada.

## Índice

- [Introdução](#introdução)
- [Algoritmos](#algoritmos)
  - [Hill Climbing](#hill-climbing)
  - [Algoritmo Genético](#algoritmo-genético)
  - [Têmpera Simulada](#têmpera-simulada)
- [Configuração](#configuração)
  - [Ambiente Virtual](#ambiente-virtual)
  - [Requisitos](#requisitos)
- [Uso](#uso)
- [Observação](#observação)
- [Contribuições](#contribuições)
- [Feito por](#feito-por)

## Introdução

O Problema do Caixeiro Viajante (TSP) é um problema clássico de otimização onde o objetivo é encontrar a rota mais curta que visita um conjunto de cidades e retorna à cidade de origem. Este repositório fornece uma solução para o TSP usando três algoritmos diferentes:

- Hill Climbing
- Algoritmo Genético
- Têmpera Simulada

## Algoritmos

### Hill Climbing

O Hill Climbing é um algoritmo de busca local que começa com uma solução arbitrária e, iterativamente, faz pequenas mudanças na solução, aceitando a mudança se ela melhorar a solução. Esse processo continua até que não se encontrem mais melhorias.

### Algoritmo Genético

O Algoritmo Genético é inspirado pelo processo de seleção natural. Ele usa técnicas como seleção, crossover e mutação para evoluir uma população de soluções em direção a soluções melhores ao longo de sucessivas gerações.

### Têmpera Simulada

A Têmpera Simulada é uma técnica de otimização que imita o processo de têmpera na metalurgia. Ela começa com uma "temperatura" alta e gradualmente esfria, aceitando não apenas soluções melhores, mas também piores com uma probabilidade que diminui com a temperatura. Isso permite que o algoritmo escape de ótimos locais.

## Configuração

### Ambiente Virtual

Para garantir um ambiente consistente e isolado para a execução deste projeto, é recomendável usar um ambiente virtual Python.

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
## Uso

1. Para iniciar o programa, execute:
    ```bash
    python3 main.py #No Windows: python main.py

2. Escolha o algoritmo de busca:
    Escolha o algoritmo para resolver o problema do Caixeiro Viajante:
    0 - Sair
    1 - Hill Climbing
    2 - Algoritmo Genético
    3 - Têmpera Simulada
    Digite a sua escolha: 

## Observação

Nós utilizamos os dados 'FIVE' disponíveis neste [site](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Feito por

Áquilas Rodrigues Jucá: GitHub(https://github.com/aquilasjuca)

Kevin de Freitas Sales: GitHub(https://github.com/Kevin439560)

Thomas Henrique Carvalho Pinheiro: GitHub(https://github.com/Thomashq)

