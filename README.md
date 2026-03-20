Relatório de Computação Paralela

Análise Paralela de Arquivos de Log

Campo	Informação
Disciplina	Computação Paralela e Distribuída
Aluno	Kaio Kevin
Professor	Rafael Marconi Ramos
Data	14/03/2026
1. Descrição do Problema

O objetivo deste trabalho foi analisar arquivos de log, contabilizando:

Número total de linhas

Número total de palavras

Número total de caracteres

Frequência das palavras-chave: erro, warning, info

Comparando duas abordagens:

Algoritmos utilizados

Serial: processamento sequencial de arquivos

Paralelo: processamento simultâneo com múltiplos processos

Entradas utilizadas

Pasta log2 contendo 1000 arquivos de log

Total processado:

10.000.000 linhas

200.000.000 palavras

1.366.663.305 caracteres

Objetivo da paralelização

Reduzir o tempo total de processamento distribuindo os arquivos entre múltiplos processos.

2. Ambiente Experimental
Item	Descrição
Processador	Intel Core i5-12450
Núcleos	12 threads lógicas
Memória RAM	16 GB
Sistema Operacional	Windows 11
Linguagem	Python 3.13
Biblioteca	multiprocessing
3. Metodologia de Testes
Medição de tempo

Utilizou-se:

time.time()
Configurações testadas

2 processos

4 processos

8 processos

12 processos

Condições

Processamento paralelo por arquivo

Uso de multiprocessing.Pool

Execução local

4. Resultados Experimentais
Dataset (1000 arquivos de log)
Processos	Tempo (s)	Speedup	Eficiência
2	51.0305	0.3404	0.1702
4	28.4915	0.6094	0.1523
8	18.9419	0.9166	0.1146
12	16.8709	1.0294	0.0858
5. Cálculo
Speedup
Speedup(p) = T(1) / T(p)
Eficiência
Eficiência(p) = Speedup(p) / p
6. Análise dos Resultados

O aumento de processos reduziu o tempo total de execução

Melhor desempenho observado com 12 processos

Ganho de desempenho foi limitado (Speedup ≈ 1.03)

Observações importantes

Overhead de criação de processos impacta desempenho

Acesso ao disco (I/O) limita o ganho

Paralelismo não escala linearmente

7. Conclusão

A paralelização trouxe ganhos modestos de desempenho.

Melhor configuração: 12 processos

Eficiência caiu conforme aumentou o paralelismo

Gargalo principal: I/O de arquivos + overhead
