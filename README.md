# Relatório de Computação Paralela

## Soma Paralela de Números em Arquivo

---

| Campo      | Informação                        |
|------------|-----------------------------------|
| Disciplina | Computação Paralela e Distribuída |
| Aluno      | Kaio kevin                        |
| Professor  | Rafael Marconi Ramos              |
| Data       | 14/03/2026                        |

---

## 1. Descrição do Problema

Calcular a soma de todos os inteiros de um arquivo de texto (um número por linha), comparando as versões serial e paralela.

**Algoritmo utilizado:**
- **Serial:** leitura linha a linha com acumulação sequencial
- **Paralelo:** divisão do arquivo em N fatias por bytes, processamento simultâneo e soma dos resultados parciais

**Entradas utilizadas:**
- `numero1.txt` — 1.000.000 de números (desenvolvimento)
- `numero2.txt` — 10.000.000 de números (análise de desempenho)

**Complexidade:** O(n) serial — O(n/p) por processo na versão paralela

Objetivo da paralelização:
Reduzir o tempo de leitura e processamento do arquivo distribuindo a carga entre múltiplos processos, aproveitando os núcleos disponíveis no processador. 


## 2. Ambiente Experimental

| Item | Descrição |
|------|-----------|
| Processador | Intel Core i5-12450 (12ª Geração) |
| Número de núcleos | 12 núcleos lógicos (8 núcleos físicos: 4 P-cores + 4 E-cores) |
| Memória RAM | 16 GB |
| Sistema Operacional | Windows 11 |
| Linguagem utilizada | Python 3.14 |
| Biblioteca de paralelização | multiprocessing (módulo padrão do Python) |
| Versão do interpretador | Python 3.14 (CPython) |


3. Metodologia de Testes
Medição do tempo:

Utilizada a função time.perf_counter() do Python, que fornece alta resolução de tempo em segundos.
O tempo medido compreende apenas a fase de processamento (leitura + soma), excluindo inicialização do programa.

Número de execuções:

Cada configuração foi executada uma vez, registrando o tempo obtido diretamente.

Configurações testadas:

1 thread/processo — versão serial
2 threads/processos
4 threads/processos
8 threads/processos
12 threads/processos

Condições de execução:

Máquina com uso normal do sistema operacional Windows 11.
Módulo multiprocessing do Python utilizado para criação e gerenciamento dos processos.
A divisão do arquivo foi feita por posição de bytes com alinhamento em quebras de linha para evitar cortes em números.


## 4. Resultados Experimentais

### 4.1 numero1.txt — 1 milhão de números (Soma: -88)

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|:-----------------:|:---------:|:-------:|:----------:|
| 1 (serial)        | 0.105798  | 1.0000  | 1.0000     |
| 2                 | 0.416220  | 0.2542  | 0.1271     |
| 4                 | 0.470866  | 0.2247  | 0.0562     |
| 8                 | 0.545442  | 0.1940  | 0.0242     |
| 12                | 0.612147  | 0.1728  | 0.0144     |

### 4.2 numero2.txt — 10 milhões de números (Soma: 5384)

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|:-----------------:|:---------:|:-------:|:----------:|
| 1 (serial)        | 1.093962  | 1.0000  | 1.0000     |
| 2                 | 1.095258  | 0.9988  | 0.4994     |
| 4                 | 0.782128  | 1.3987  | 0.3497     |
| 8                 | 0.899968  | 1.2156  | 0.1519     |
| 12                | 0.963471  | 1.1354  | 0.0946     |

## 5. Cálculo de Speedup e Eficiência

**Speedup:** `Speedup(p) = T(1) / T(p)`

Onde T(1) é o tempo da execução serial e T(p) é o tempo com p threads/processos.

**Eficiência:** `Eficiência(p) = Speedup(p) / p`

Onde p é o número de threads ou processos.

---

## 6. Análise dos Resultados

### 6.1 numero1.txt (1 milhão de números)
1 milhão de números (Soma: -88)

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|:-----------------:|:---------:|:-------:|:----------:|
| 1 (serial)        | 0.105798  | 1.0000  | 1.0000     |
| 2                 | 0.416220  | 0.2542  | 0.1271     |
| 4                 | 0.470866  | 0.2247  | 0.0562     |
| 8                 | 0.545442  | 0.1940  | 0.0242     |
| 12                | 0.612147  | 0.1728  | 0.0144     |


### 6.2 numero2.txt (10 milhões de números)

10 milhões de números (Soma: 5384)

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
|:-----------------:|:---------:|:-------:|:----------:|
| 1 (serial)        | 1.093962  | 1.0000  | 1.0000     |
| 2                 | 1.095258  | 0.9988  | 0.4994     |
| 4                 | 0.782128  | 1.3987  | 0.3497     |
| 8                 | 0.899968  | 1.2156  | 0.1519     |
| 12                | 0.963471  | 1.1354  | 0.0946     |
## 7. Conclusão

No cenário de 1 milhão de números, observou-se que a execução serial foi, em todos os casos, mais rápida que a paralela. Isso ocorre devido ao fenômeno do overhead de gerenciamento: o tempo necessário para o sistema operacional criar as threads, dividir os dados na memória e realizar a sincronização final da soma é maior do que o tempo que o processador leva para somar os números sequencialmente. Note que, conforme o número de threads aumentou de 2 para 12, a eficiência despencou de 0.1271 para 0.0144, indicando que o excesso de divisões prejudicou o desempenho em uma carga de trabalho considerada pequena para os processadores modernos.

