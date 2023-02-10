with open("dados.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

count = 0
alfabeto = None
estados = None
inicial = None
finais = None
transicoes = []

for line in lines:
    
    if count == 0:
        reject = "alfabeto="
        for i in range(0, len(reject)):
            line = line.replace(reject[i], "")

        line = line.split('\n')
        line = line[0]

        alfabeto = list(map(str, line.split(",")))
        count += 1

    elif count == 1:
        reject = "estados="
        for i in range(0, len(reject)):
            line = line.replace(reject[i], "")

        line = line.split('\n')
        line = line[0]
        
        estados = list(map(str, line.split(",")))
        count += 1
    
    elif count == 2:
        reject = "inicial="
        for i in range(0, len(reject)):
            line = line.replace(reject[i], "")

        line = line.split('\n')
        line = line[0]
        
        inicial = str(line)
        count += 1
    
    elif count == 3:
        reject = "finais="
        for i in range(0, len(reject)):
            line = line.replace(reject[i], "")

        line = line.split('\n')
        line = line[0]
        
        finais = list(map(str, line.split(",")))
        count += 1
    
    elif count == 4: #linha "transicoes"
        count += 1

    elif count == 5:
        transicoes.append(line[0])
        transicoes.append(line[2])
        transicoes.append(line[4])

conta_alfabeto = None
percorre_transicoes = None
novos_estados = []

def estado_inicial(conta_alfabeto, percorre_transicoes):
    x = 0
    while x < len(estados):
        if inicial == estados[x]:
            return afd_valido(conta_alfabeto, percorre_transicoes)
        else:
            x += 1
    if x == len(estados):
        return print("O estado inicial não está dentro dos estados descritos")

def afd_valido(conta_alfabeto,percorre_transicoes):
    afd_ok = 0
    percorre_estados = 0
    while percorre_estados < len(estados):
        if conta_alfabeto != len(alfabeto) and percorre_transicoes == len(transicoes):
            return print("O AFD descrito nao é válido")    
        analisa_estado = estados[percorre_estados]
        percorre_transicoes = 0
        conta_alfabeto = 0
        while percorre_transicoes < len(transicoes):
            if analisa_estado == transicoes[percorre_transicoes]:
                percorre_alfabeto = 0
                while percorre_alfabeto < len(alfabeto):
                    if transicoes[percorre_transicoes+2] == alfabeto[percorre_alfabeto]:
                        conta_alfabeto += 1
                        percorre_transicoes += 3
                        percorre_alfabeto = len(alfabeto)
                        if conta_alfabeto == len(alfabeto):
                            percorre_estados += 1
                            percorre_transicoes = len(transicoes)
                            afd_ok += 1
                    else:
                        percorre_alfabeto += 1
            else:
                percorre_transicoes += 3
    if afd_ok == len(estados):
        print("")
        print("O AFD descrito é válido")
        return primeiro_passo(novos_estados)

def primeiro_passo(novos_estados):
    x = 0
    k = 1
    
    while x < len(estados) - 1:
        k = x + 1
        while k < len(estados):
            contagem = 0
            contagem_igual = 0
            y = 0
            while y < len(finais):
                if estados[x] == finais[y] and estados[k] == finais[y] or estados[x] != finais[y] and estados[k] != finais[y]:
                    y += 1
                    contagem += 1
                    if contagem == len(finais):
                        novos_estados.append(estados[x])
                        novos_estados.append(estados[k])
                        print("")
                        print("O estado " + estados[x] + " e o estado " + estados[k] + " não são estados finais, logo se encaixam no primeiro passo da minimização de AFD")
                    
                else:
                    if estados[x] == finais[y]:
                        contagem_igual += 1
                    if estados[k] == finais[y]:
                        contagem_igual +=1
                    y += 1
                    if contagem_igual == 2:
                        novos_estados.append(estados[x])
                        novos_estados.append(estados[k])
                        print("")
                        print("O estado " + estados[x] + " e o estado " + estados[k] + " são estados finais, logo se encaixam no primeiro passo da minimização de AFD")
                        
            k += 1
        x += 1

    print("")
    print(novos_estados)
    
    return segundo_passo(novos_estados)

def segundo_passo(novos_estados):
    lista = []
    leitura = []
    x = 0
    conta = 0
    while x < len(novos_estados):
        y = 0
        while y < len(transicoes):
            if novos_estados[x] == transicoes[y]:
                    elemento = transicoes[y+2]
                    leitura.append(transicoes[y+1])
                    z = 0
            while z < len(transicoes):
                if novos_estados[x+1] == transicoes[z]:
                    if elemento == transicoes[z+2]:
                        leitura.append(transicoes[z+1])



                        f = 0
                        if leitura[0] == leitura[1]:
                                f = len(novos_estados)
                                conta += 1
                                z = len(transicoes)
                                if conta == 2:
                                    conta = 0
                                    x += 2
                                    y = len(transicoes)
                        while f < len(novos_estados):
                            if leitura[0] == novos_estados[f]:
                                if f % 2 == 0:
                                    if novos_estados[f+1] == leitura[1]:
                                            f = len(novos_estados)
                                            leitura = []
                                            conta += 1
                                            if conta == 2:
                                                    conta = 0
                                                    x += 2
                                                    y = len(transicoes)
                                            z = len(transicoes)
                                    else:
                                        f += 1
                                        if f == len(novos_estados):
                                            lista.append(novos_estados[x])
                                            lista.append(novos_estados[x+1])
                                            x += 2
                                            y = len(transicoes)
                                            z = len(transicoes)
                                    
                                    
                                else:
                                    if novos_estados[f-1] == leitura[1]:
                                        f = len(novos_estados)
                                        leitura = []
                                        conta += 1
                                        if conta == 2:
                                            conta = 0
                                            x += 2
                                            y = len(transicoes)
                                        z = len(transicoes)
                                    else:
                                        f += 1
                                        if f == len(novos_estados):
                                                lista.append(novos_estados[x])
                                                lista.append(novos_estados[x+1])
                                                x += 2
                                                y = len(transicoes)
                                                z = len(transicoes)
                                                leitura = []
                                                conta = 0
                            else:
                                f += 1
                                if f == len(novos_estados):
                                                lista.append(novos_estados[x])
                                                lista.append(novos_estados[x+1])
                                                x += 2
                                                y = len(transicoes)
                                                z = len(transicoes)
                                                leitura = []
                                                conta = 0
                                                
                                
                    else:
                        z += 3
                else:
                    z += 3

            else:
                y += 3

    w = 0
    while w < len(lista):
        t = 0
        while t < len(novos_estados):
            if lista[w] == novos_estados[t]:
                if lista[w+1] == novos_estados[t+1]:
                    del novos_estados[t]
                    del novos_estados[t]
                    t = len(novos_estados)
                    w += 2

                else:
                    t += 2
            else:
                t += 2

    r = 0
    while r < len(novos_estados):
        print("")
        print("Após o segundo método aplicado para diminuir os estados ainda restaram os estados " + novos_estados[r] + novos_estados[r+1])
        r += 2

    print("")    
    print(novos_estados)

    return terceiro_passo(novos_estados)

def terceiro_passo(novos_estados):
    variavel = []
    estados_minimizados = []
    y = 0
    while y < len(novos_estados):
        if novos_estados[y] != novos_estados[y+1]:
            estados_minimizados.append(novos_estados[y] + novos_estados[y+1])
            y += 2
            if novos_estados[y] != novos_estados[y+1]:
                if novos_estados[y+2] != novos_estados[y+3]:
                    estados_minimizados.append(novos_estados[y] + novos_estados[y+1] + novos_estados[y+3])
                    y = len(novos_estados)

    z = 0
    while z < len(estados):
        if estados[z] == transicoes[-2]:
            estados_minimizados.append(transicoes[-2])
            z = len(estados)
        else:
            z += 1
    print("")
    print("Após a minimização de estados,os estados restantes são")
    print("")
    print(estados_minimizados)

    k = 0
    l = 1
    novas_transicoes = []
    while k < len(transicoes):
        if estados_minimizados[k] != estados_minimizados[k+2]:
            novas_transicoes.append(estados_minimizados[k])
            novas_transicoes.append(estados_minimizados[k])
            novas_transicoes.append(transicoes[l+1])
            if estados_minimizados[k] != estados_minimizados[k + 1]:
                novas_transicoes.append(estados_minimizados[k])
                novas_transicoes.append(estados_minimizados[k+1])
                novas_transicoes.append(transicoes[l+4])
                f = 0
                while f < len(transicoes):
                    k = 1
                    if estados_minimizados[k] != estados_minimizados[k + 1]:
                        novas_transicoes.append(estados_minimizados[k])
                        novas_transicoes.append(estados_minimizados[k])
                        novas_transicoes.append(transicoes[l+1])
                        if estados_minimizados[k] != estados_minimizados[k-1]:
                            novas_transicoes.append(estados_minimizados[k])
                            novas_transicoes.append(estados_minimizados[k+1])
                            novas_transicoes.append(transicoes[l+4])
                            u = 0
                            while u < len(transicoes):
                                k = 2
                                while l < len(novos_estados)- 2:
                                    if estados_minimizados[k] == estados_minimizados[k]:
                                        novas_transicoes.append(estados_minimizados[k])
                                        novas_transicoes.append(estados_minimizados[k])
                                        novas_transicoes.append(transicoes[l+1])
                                        l += 3
                                        u = len(transicoes)
                                        f = len(transicoes)
                                        if l == 7:
                                            k = len(transicoes)

                                    else:
                                        l += 3
                                
                                
                                

                        else:
                            f += 1
                        

                    else:
                        f += 1
                    
                

            else:
                k += 1
        else:
            k += 1
        
    print("")
    print("  --|"+estados_minimizados[0]+"| ----> ||"+estados_minimizados[1]+"|| ----> |"+estados_minimizados[2]+"|") 

    print("")  
    print("Alunos: João Victor Dias Gonçalves, Igor Edmundo Castilho")
    print("")



    

    
                
    

estado_inicial(conta_alfabeto, percorre_transicoes)