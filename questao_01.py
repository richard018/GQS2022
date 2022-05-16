def reposicao(item_quantidade):

    if(len(item_quantidade) == 0):
        return 0
    resultado = 0
    estocar = item_quantidade[0][1]
    for elem in item_quantidade:
        if(elem[1] < estocar):
            estocar = elem[1]
            resultado += 1
    return resultado





