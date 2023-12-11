import numpy as np

def dois_dados() -> int:
    resultados = np.random.randint(1,7,size=2)
    soma = np.sum(resultados)
    return soma

#jogos = np.array(dois_dados())

lancamentos = ""
while type(lancamentos) is not int:
    try:
        lancamentos = int(input('Insira o número de lançamentos de dois dados: '))
        assert lancamentos > 0
    except:
        print('Por favor insira um número inteiro e maior que 0')
        lancamentos = ""

jogos = np.empty(lancamentos, dtype = int)

for x in range(lancamentos):
    jogos[x] = dois_dados()

lancamento, ocorrencia = np.unique(jogos,return_counts=True)

print(f'A média dos resultados é: {jogos.mean()}')
print(f'O lançamento máximo foi: {jogos.max()}')
print(f'O lançamento mínimo foi: {jogos.min()}')
print('Número de vezes de cada lançamento:')
print('Valor - Ocorrências')
for valor, qtd in zip(lancamento, ocorrencia):
    print(f'{valor:5} - {qtd}')