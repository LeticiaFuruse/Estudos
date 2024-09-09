lista = [10,20,30,40,50]
# soma = sum(lista)
# print("soma: ", soma)
def soma(lista):
    total = 0
    for i in lista:
        total = total+ i
    return total
    
print(soma(lista))