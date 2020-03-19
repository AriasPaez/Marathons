cant_cases = int(input())
dic_teclado = {0:" ",1:",",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

for i in range(cant_cases):
    line=input()
    salida = ""
    # Recorre el string
    for l in range(len(line)):

        #recorre el diccionario para encontrar la letra
        for x_dic in range(0, len(dic_teclado)):
            #print(line[l],"[",l, "] : ", dic_teclado.get(x_dic)," , ",x_dic)
            if line[l] in dic_teclado.get(x_dic):
                # print("ENCONTRADO= ",line[l], "[", l, "] : ", dic_teclado.get(x_dic), " , ", x_dic)
                # print((dic_teclado.get(x_dic).find(line[l])+1))
                vez = (dic_teclado.get(x_dic).find(line[l]) + 1)
                # print("t7am: ",len(salida),"--",salida[len(salida)-1])
                if (len(salida) > 0 and int(salida[len(salida) - 1]) == int(x_dic)):
                    salida += " "

                salida += str(x_dic) * vez

    print("Case #"+str(i+1)+":",salida)
