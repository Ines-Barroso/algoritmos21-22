# EMD = [id, dataEMD, Pnome, Unome, idade, género, morada, modalidade, clube, email, federado,resultado]

def getEMD(linha):
        novaLinha = linha.replace("\n", "") 
        emd = []
        campos = novaLinha.split(",")
        emd.append("emd"+ str(int(campos[1])+1)) #campos[1] = index que ira substituir aquele id todo
        for i in range (2,len(campos)):
            emd.append(campos[i])
        return emd
    
def lerDataset():
        f = open("emd.csv")
        bd = []
        f.readline() #tirar a linha do cabeçalho\n",
        for linha in f:
            bd.append(getEMD(linha))
        return bd

    #Especifica uma função que faça a listagem no monitor dos vários registos de informação por ordem cronológica decrescente.    

def ordAno (registo):
        return registo[1]
    
def listarDataset():
        bd = lerDataset()
        print ("{:<10} {:<15} {:<25} {:<8}".format('Id','Data','Nome','Apto'))
        bd.sort(reverse = True, key = ordAno)
        for registo in bd:
            nome = registo [2] + " " + registo [3]
            print ("{:<10} {:<15} {:<25} {:<8}".format(registo[0],registo [1],nome,registo[11]))

    # Especifica uma função que, dado o id de um EMD, coloca a sua informação no monitor."
 
def consultarDataset(id):
        bd = lerDataset()
        stop = False
        i = 0
        while not stop:
            if bd[i][0] == id :
                stop = True
            else:
                i = i+1 
        return bd[i]          

    #Especifica um função que dá como resultado uma lista de modalidades ordenada alfabeticamente e sem repetições."

def modalidades():
        bd = lerDataset()
        M = []
        for m in bd :
            if m[7] not in M :
                M.append(m[7])
        M.sort()
        return M

    #Especifica uma função que dá como resultado uma lista de pares indicando quantos EMD estão registados em cada modalidade."

def distribPorModalidade():
        bd = lerDataset()
        distribuicao = {}
        for registo in bd:
            if registo[7] in distribuicao.keys():
                distribuicao[registo[7]] = distribuicao[registo[7]]+1
            else:
               distribuicao[registo[7]] = 1
        return distribuicao #{modalidade : numero de emd}

    #Especifica uma função que dá como resultado uma lista de pares indicando quantos EMD estão registados por cada clube."

def distribPorClube():
        bd = lerDataset()
        distribuicao = {}
        for registo in bd:
            if registo[8] in distribuicao.keys():
                distribuicao[registo[8]] = distribuicao[registo[8]]+1
            else:
                distribuicao[registo[8]] = 1
        return distribuicao #{clube : numero de emd}

    #Especifica uma função que dá como resultado uma lista de pares indicando quantos EMD estão registados por cada ano."

def ordAno (registo):
        return registo[1]
    
def distribPorAno():
        bd = lerDataset()
        distribuicao = {}
        bd.sort(reverse = True, key = ordAno) #por do mais recente para o menos
        for registo in bd:
            if registo[1][0:4] in distribuicao.keys():
                distribuicao[registo[1][0:4]] = distribuicao[registo[1][0:4]]+1
            else:
                distribuicao[registo[1][0:4]] = 1
        return distribuicao #{ano : numero de emd}

    #Especifica uma função que permita calcular uma distribuição por qualquer um dos campos da BD."

def buscarCampo (campo):
        if campo == "Ano":
            return distrib(1)
        elif campo == "Idade":
            return distrib(4)
        elif campo == "Genero" :
            return distrib(5)
        elif campo == "Morada":
            return distrib(6)
        elif campo == "Modalidade":
            return distrib(7)
        elif campo == "Clube" :
            return distrib(8)
        elif campo == "Federado":
            return distrib(10)
        elif campo == "Resultado" :
            return distrib(11)

def distrib(n):
        bd = lerDataset()
        distribuicao = {}
        if n == 1 :
            return distribPorAno()
        elif n == 7 :
            return distribPorModalidade()
        elif n == 8 :
            return distribPorClube()
        else:
            for registo in bd:
                if registo[n] in distribuicao.keys():
                    distribuicao[registo[n]] = distribuicao[registo[n]]+1
                else:
                    distribuicao[registo[n]] = 1
            return distribuicao #{campo : numero de emd}

    #Especifica uma função que faz o plot dum gráfico com a distribuição de emd por modalidade."

def plotDistribPorModalidade():
        import matplotlib.pyplot as plt
        distribuicao = distribPorModalidade()
        # heights of bars
        modalidade = distribuicao.keys()
        height = []
        for m in modalidade :
            height.append(m)   

        # labels for bars\n",
        numero_emd = distribuicao.values() 
        x = []
        i = 1
        tick_label = []
        for emd in numero_emd:
            tick_label.append(emd)
            x.append(i)
            i = i+1
    
        # plotting a bar chart\n",
        plt.bar(x,height, tick_label = tick_label, width = 0.8)
        # naming the x-axis\n",
        plt.xlabel('Numero emd')
        # naming the y-axis\n",
        plt.ylabel('Modalidades')
        # plot title\n",
        plt.title('Distribuição por Modalidade')
        plt.show() 

    #Especifica uma função que faz o plot dum gráfico com a distribuição passada como argumento.\n",

def plotDistrib(campo):
        import matplotlib.pyplot as plt
        if campo == "Modalidade":
            plotDistribPorModalidade()
        elif campo == "Clube":
            distribuicao = buscarCampo(campo)
            # heights of bars
            clubes = distribuicao.keys()
            height = []
            for c in clubes :
                height.append(c)   

            # labels for bars\n",
            numero_emd = distribuicao.values() 
            x = []
            i = 1
            tick_label = []
            for emd in numero_emd:
                tick_label.append(emd)
                x.append(i)
                i = i+1
    
            # plotting a bar chart\n",
            plt.bar(x,height, tick_label = tick_label, width = 0.8)
            # naming the x-axis\n",
            plt.xlabel('Numero emd')
            # naming the y-axis\n",
            plt.ylabel('Clubes')
            # plot title\n",
            plt.title('Distribuição por Clube')
            plt.show()
        else:
        # heights of bars\n",
            distribuicao = buscarCampo(campo)
            numero_emd = distribuicao.values()
            height = []
            for emd in numero_emd :
                height.append(emd)  
    
        # labels for bars\n",
            campos = distribuicao.keys()
            x = []
            i = 1
            tick_label = []
            for c in campos:
                tick_label.append(c)
                x.append(i)
                i = i+1
            # plotting a bar chart\n",
            plt.bar(x,height, tick_label = tick_label, width = 0.8)
            # naming the x-axis\n",
            plt.xlabel(campo)
            # naming the y-axis\n",
            plt.ylabel('Numero emd')
            # plot title\n",
            plt.title('Distribuição por ' + campo)
            plt.show()

