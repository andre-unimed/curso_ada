# Databricks notebook source
# MAGIC %md
# MAGIC # Hands-On
# MAGIC
# MAGIC Você foi designado para realizar a limpeza e preparação de dados de dois conjuntos de dados (base1.csv e base2.csv) distintos que representam informações relacionadas a risco de crédito.
# MAGIC
# MAGIC Seu objetivo é ler os dois conjuntos de dados usando a biblioteca Pandas, realizar a concatenação dos dados, lidar com valores duplicados e faltantes, além de verificar a presença de outliers nos dados combinados.
# MAGIC
# MAGIC ____
# MAGIC
# MAGIC ## Passos a serem seguidos:
# MAGIC
# MAGIC 1. **Leitura dos Arquivos:** Utilize a biblioteca Pandas para ler os dois arquivos de dados: 'base1.csv' e 'base2.csv', que estão no diretório datasets, no repositório do módulo.
# MAGIC 2. **Concatenação dos Dados:** Concatene os dois conjuntos de dados em um único DataFrame, verificando se os dados possuem a mesma estrutura para uma concatenação adequada.
# MAGIC 3. **Tratamento de Dados Duplicados:** Verifique se há linhas duplicadas no DataFrame combinado e remova-as, mantendo a primeira ocorrência.
# MAGIC 4. **Tratamento de Valores Faltantes:** Identifique e lide com os valores faltantes no DataFrame combinado. Preencha os valores ausentes com estratégias apropriadas (média, mediana, valor específico etc.) dependendo do contexto dos dados.
# MAGIC 5. **Verificação de Outliers:** Utilize métodos estatísticos ou gráficos (como boxplots) para identificar a presença de outliers nos dados. Considere se eles são significativos para a análise ou se precisam ser tratados de alguma forma.

# COMMAND ----------

import pandas as pd
import numpy as np

# COMMAND ----------

# MAGIC %md
# MAGIC Leitura dos Arquivos: Utilize a biblioteca Pandas para ler os dois arquivos de dados: 'base1.csv' e 'base2.csv', que estão no diretório datasets, no repositório do módulo.

# COMMAND ----------

df_base1 = pd.read_csv('base1.csv')
df_base2 = pd.read_csv('base2.csv')

df_base1.drop(df_base1.columns[[0,1]], axis=1, inplace=True)
df_base2.drop(df_base2.columns[[0,1]], axis=1, inplace=True)


# COMMAND ----------

# MAGIC %md
# MAGIC Concatenação dos Dados: Concatene os dois conjuntos de dados em um único DataFrame, verificando se os dados possuem a mesma estrutura para uma concatenação adequada

# COMMAND ----------

df_base_concatenada = pd.concat([df_base1,df_base2], ignore_index=True)

df_base_concatenada

# COMMAND ----------

# MAGIC %md
# MAGIC Tratamento de Dados Duplicados: Verifique se há linhas duplicadas no DataFrame combinado e remova-as, mantendo a primeira ocorrência

# COMMAND ----------

df_base_concatenada.loc[df_base_concatenada.duplicated()]

#dataframe vazio significa que não existem linhas duplicadas

# COMMAND ----------

df_base_sem_duplicada = df_base_concatenada.drop_duplicates()
#apaga linhas duplicadas (toda a linha sendo verificada)
df_base_sem_duplicada

# COMMAND ----------

# MAGIC %md
# MAGIC Tratamento de Valores Faltantes: Identifique e lide com os valores faltantes no DataFrame combinado. Preencha os valores ausentes com estratégias apropriadas (média, mediana, valor específico etc.) dependendo do contexto dos dados

# COMMAND ----------

df_base_sem_duplicada.info()

#identificando onde estão os valores faltantes, nesse caso nas colulas 'Saving accounts' e 'Checking account'

# COMMAND ----------

df_base_sem_duplicada.value_counts('')

# COMMAND ----------


