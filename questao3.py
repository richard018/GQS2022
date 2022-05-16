def soma_vendas(total_vendas):
    soma =  total_vendas[0][1] + total_vendas[1][1] + total_vendas[2][1] + total_vendas[3][1]

    soma_arredondado = round(soma, 1)

    return soma_arredondado