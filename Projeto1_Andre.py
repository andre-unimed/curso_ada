import numpy as np

def dois_dados() -> int:
    resultados = np.random.randint(1,7,size=2)
    soma = np.sum(resultados)
    return soma

jogos = np.array(dois_dados())

lancamentos = ""
while type(lancamentos) is not int:
    try:
        lancamentos = int(input('Insira o número de lançamentos de dois dados: '))
    except:
        print('Por favor insira um número inteiro')

for x in range(lancamentos-1):
    jogos = np.append(jogos,dois_dados())

lancamento, ocorrencia = np.unique(jogos,return_counts=True)

#print(jogos)
print(f'A média dos resultados é: {jogos.mean()}')
print(f'O lançamento máximo foi: {jogos.max()}')
print(f'O lançamento mínimo foi: {jogos.min()}')
print('Número de vezes de cada lançamento:')
for valor, qtd in zip(lancamento, ocorrencia):
    print(f'{valor} - {qtd}')

