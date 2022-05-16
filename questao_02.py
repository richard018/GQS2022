def percentual_vendas(vendas):
    total_venda = 0
    for elem in vendas:
        total_venda += elem[2]
    percentual_lista = []
    for elem in vendas:
        if(total_venda == 0):
            percentual_lista.append((elem[1], 0))
        else:
            percentual_lista.append((elem[1], round(elem[2]/total_venda, 4)))

    return percentual_lista