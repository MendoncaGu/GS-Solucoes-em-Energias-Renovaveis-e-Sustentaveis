# GS-Solucoes-em-Energias-Renovaveis-e-Sustentaveis

# Trabalho feito por Ângelo Malta Reina - RM 570769 & Gustavo Mendonça Duarte - RM 570561

# 🚀 Mission Control AI

## Monitoramento Energético Espacial

O **Mission Control AI** é um simulador de monitoramento de sistemas críticos de uma missão espacial. O projeto foi desenvolvido em Python com o objetivo de demonstrar conceitos de programação, análise de dados operacionais e cálculos energéticos aplicados a um cenário inspirado em centros de controle de missões.

Além de avaliar a saúde dos sistemas da nave, o programa realiza análises elétricas e gera relatórios completos sobre o desempenho da missão.

---

## 🎯 Objetivo do Projeto

Imagine que você faz parte da equipe responsável por monitorar uma estação espacial.

A cada ciclo de operação, diversos parâmetros precisam ser analisados:

* 🌡️ Temperatura interna
* 📡 Comunicação com a base
* 🔋 Sistema de energia
* 🫁 Suporte de oxigênio
* ⚙️ Estabilidade operacional

Além disso, o sistema também monitora informações elétricas como:

* Tensão
* Corrente
* Fator de potência
* Consumo de energia
* Rendimento do motor

Com base nesses dados, o programa identifica riscos, classifica a situação da missão e sugere ações corretivas quando necessário.

---

## 🧠 Conceitos de Programação Utilizados

Este projeto é excelente para estudantes iniciantes porque utiliza diversos conceitos fundamentais da programação:

### Variáveis

Armazenamento de informações coletadas durante cada ciclo.

### Estruturas Condicionais

Uso de `if`, `elif` e `else` para classificar situações como:

* NORMAL
* ATENÇÃO
* CRÍTICO

### Laços de Repetição

Uso de `for` e `while` para:

* Ler entradas do usuário
* Processar múltiplos ciclos
* Gerar análises automáticas

### Funções

O código foi dividido em funções especializadas para tornar a manutenção mais simples e organizada.

Exemplos:

* `analisar_temperatura()`
* `analisar_comunicacao()`
* `calcular_potencias()`
* `gerar_relatorio_final()`

### Estruturas de Dados

Utilização de:

* Listas (`list`)
* Dicionários (`dict`)
* Tuplas (`tuple`)

para armazenar e processar informações da missão.

---

## ⚡ Cálculos Elétricos Implementados

O sistema também realiza cálculos comuns da engenharia elétrica.

### Potência Aparente

S = U × I

Onde:

* U = tensão (V)
* I = corrente (A)

---

### Potência Ativa

P = S × FP

Onde:

* FP = fator de potência

---

### Potência Reativa

Q = √(S² − P²)

---

### Rendimento do Motor

η = Potência Útil / Potência Ativa

---

### Energia Consumida

E = P × Δt

Esses cálculos permitem avaliar a eficiência energética dos sistemas monitorados.

---

## 🚨 Sistema de Classificação de Risco

Cada área analisada recebe uma classificação:

| Status  | Significado                          |
| ------- | ------------------------------------ |
| NORMAL  | Sistema funcionando adequadamente    |
| ATENÇÃO | Possível problema em desenvolvimento |
| CRÍTICO | Falha grave que exige ação imediata  |

A soma dos riscos determina a situação geral da missão.

### Classificação Final

| Pontuação  | Resultado         |
| ---------- | ----------------- |
| 0 a 2      | MISSÃO ESTÁVEL    |
| 3 a 5      | MISSÃO EM ATENÇÃO |
| Acima de 5 | MISSÃO CRÍTICA    |

---

## 📊 Relatório Final

Após todos os ciclos analisados, o programa gera automaticamente:

* Médias operacionais
* Médias energéticas
* Ciclo mais crítico
* Tendência da missão
* Área mais afetada
* Classificação final
* Estatísticas de risco

Isso permite uma visão completa do desempenho da missão durante todo o período monitorado.

## 👨‍🚀 Conclusão

O Mission Control AI é um projeto educacional que combina programação, análise de sistemas e conceitos energéticos em um cenário de exploração espacial.

Mais do que apenas um exercício de código, ele demonstra como softwares podem monitorar ambientes críticos, detectar riscos e auxiliar na tomada de decisões, habilidades presentes em aplicações reais da indústria, da engenharia e da exploração espacial.
