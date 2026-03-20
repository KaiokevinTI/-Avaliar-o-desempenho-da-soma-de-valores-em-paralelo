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

| Métrica        | Valor |
|---------------|------|
| Linhas        | 10.000.000 |
| Palavras      | 200.000.000 |
| Caracteres    | 1.366.663.305 |

---

### 🎯 Objetivo

Reduzir o tempo total de execução utilizando paralelismo baseado em múltiplos processos.

---

## 💻 2. Ambiente Experimental

| Item              | Descrição                |
|------------------|------------------------|
| Processador      | Intel Core i5-12450    |
| Núcleos          | 12 threads lógicas     |
| Memória RAM      | 16 GB                  |
| Sistema Operacional | Windows 11          |
| Linguagem        | Python 3.13            |
| Biblioteca       | multiprocessing        |

---
## 🧪 3. Metodologia

### ⏱️ Medição de tempo
python
time.time() 

⚙️ Configurações testadas

2 processos

4 processos

8 processos

12 processos

📌 Condições

Processamento paralelo por arquivo

Uso de multiprocessing.Pool

Execução local

📈 4. Resultados Experimentais
📊 Dataset: 1000 arquivos

| Processos | Tempo (s) | Speedup | Eficiência |
| --------- | --------- | ------- | ---------- |
| 2         | 51.0305   | 0.3404  | 0.1702     |
| 4         | 28.4915   | 0.6094  | 0.1523     |
| 8         | 18.9419   | 0.9166  | 0.1146     |
| 12        | 16.8709   | 1.0294  | 0.0858     |

🧮 5. Fórmulas
Speedup
Speedup(p) = T(1) / T(p)
Eficiência
Eficiência(p) = Speedup(p) / p
🔍 6. Análise dos Resultados

Houve redução no tempo com aumento de processos

Melhor desempenho com 12 processos

Speedup máximo ≈ 1.03

⚠️ Limitações observadas

Overhead de criação de processos

Gargalo de leitura de disco (I/O)

Ganho não linear

🧾 7. Conclusão

A paralelização apresentou ganhos limitados, devido principalmente ao custo de I/O e overhead.

✔️ Pontos principais

Melhor configuração: 12 processos

Eficiência diminui com mais processos

Paralelismo não escala linearmente
