lista = [-61, -62, 89, -85, 86, 17, -57, 68]
# lista =  [-2, -3, 4, -1, -2, 1, 5, -3]

subarray = []

def encontra_subarray(i, j, lista):
    if(i==j):
        return i, j, lista[i]

    meio = (i+j) // 2
    #passar as somas para o maiorSoma
    iEsq, jEsq, somaEsq = encontra_subarray(i,meio,lista)
    iDir, jDir, somaDir = encontra_subarray(meio+1, j, lista)

    return MaiorSoma(iEsq, jEsq, jDir,lista)
    
def MaiorSoma(iEsq, jEsq, jDir,lista):
    #inicializar com a soma da esquerda da direita e com a soma da esquerda no proximo loop
    maiorSoma = 0
    soma = 0
    bestI = iEsq
    bestJ = jEsq
    
    for j in range(iEsq,jDir+1):
        soma += lista[j]
        if(soma >= maiorSoma):
            maiorSoma = soma
            bestJ = j

    soma = 0
    for i in range(jDir,iEsq-1, -1):
        soma += lista[i]
        if(soma >= maiorSoma):
            maiorSoma = soma
            bestI = i
            bestJ = jDir

    return bestI, bestJ, maiorSoma

def maior_subarray(lista):
    i, j, soma = encontra_subarray(0, len(lista)-1, lista)
    return lista[i:j + 1], soma

print(maior_subarray(lista))