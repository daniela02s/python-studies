
# DESAFIO 1: Você precisa de uma função que irá receber um array de inteiros, nums,
# de comprimento n que abrange de 0 a n com um número faltando. 
# Escreva uma função missing_number que retorna o número faltando no array.

# Input:
# nums = [1,2,3,4,5,6,8] 

# missing_number(nums)

# Output: 
# 7​

def missing_number(nums):
    n = len(nums)
    # Soma esperada de 0 a n
    total = n*(n+1)/2
    # Soma real dos elementos no array
    sum_of_nums = sum(nums)
    # O número que falta é a diferença
    return total - sum_of_nums

nums = [1,2,3,4,5,6,8] 

# Teste com o exemplo fornecido
nums = [1, 2, 3, 4, 5, 6, 8]
print(f"O número faltando é: {missing_number(nums)}")