# 📊 Relatório de Computação Paralela
## Análise Paralela de Arquivos de Log

---

## 👨‍🎓 Informações

| Campo       | Informação                          |
|------------|----------------------------------|
| Disciplina | Computação Paralela e Distribuída |
| Aluno      | Kaio Kevin                        |
| Professor  | Rafael Marconi Ramos              |
| Data       | 14/03/2026                        |

---

## 🧩 1. Descrição do Problema

O objetivo deste trabalho foi analisar arquivos de log, contabilizando:

- Total de linhas  
- Total de palavras  
- Total de caracteres  
- Frequência das palavras-chave: **erro, warning, info**

### ⚙️ Abordagens

- **Serial:** processamento sequencial de arquivos  
- **Paralelo:** processamento simultâneo utilizando múltiplos processos  

---

### 📂 Entradas

- Pasta `log2` contendo **1000 arquivos de log**

**Volume total processado:**

| Métrica     | Valor            |
|------------|------------------|
| Linhas     | 10.000.000       |
| Palavras   | 200.000.000      |
| Caracteres | 1.366.663.305    |

---

### 🎯 Objetivo

Reduzir o tempo total de execução utilizando paralelismo baseado em múltiplos processos.

---

## 💻 2. Ambiente Experimental

| Item                 | Descrição             |
|----------------------|----------------------|
| Processador          | Intel Core i5-12450  |
| Núcleos              | 12 threads lógicas   |
| Memória RAM          | 16 GB                |
| Sistema Operacional  | Windows 11           |
| Linguagem            | Python 3.13          |
| Biblioteca           | multiprocessing      |

---

## 🧪 3. Metodologia

### ⏱️ Medição de Tempo

``python
time.time()

## ⚙️ Configurações Testadas

2 processos

4 processos

8 processos

12 processos

## 📌 Condições de Execução

Processamento paralelo por arquivo

Uso de multiprocessing.Pool

Execução local

Máquina com uso normal do sistema

---

### 📈 4. Resultados Experimentais

| Processos | Tempo (s) | Speedup | Eficiência |
| --------- | --------- | ------- | ---------- |
| 2         | 51.0305   | 0.3404  | 0.1702     |
| 4         | 28.4915   | 0.6094  | 0.1523     |
| 8         | 18.9419   | 0.9166  | 0.1146     |
| 12        | 16.8709   | 1.0294  | 0.0858     |


---

### 🧮 5. Cálculo

🔹 Speedup
Speedup(p) = T(1) / T(p)
🔹 Eficiência
Eficiência(p) = Speedup(p) / p


---

### 🔍 6. Análise dos Resultados

O aumento de processos reduziu o tempo total de execução

Melhor desempenho observado com 12 processos

Speedup máximo ≈ 1.03

⚠️ Limitações Observadas

Overhead de criação de processos

Gargalo de leitura de disco (I/O)

Paralelismo não escala linearmente

---

### 🧾 7. Conclusão

A paralelização apresentou ganhos limitados, devido principalmente ao custo de I/O e overhead.

## ✔️ Principais Pontos

Melhor configuração: 12 processos

Eficiência diminui conforme aumenta o número de processos

O ganho de desempenho não é proporcional ao número de processos
