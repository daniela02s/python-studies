# %% 

receita_anual = 250000
custo_operacional_mensal = 15000
despesa_variavel_mensal = 5000
depreciacao_anual = 12000

despesa_operacional_anual = (custo_operacional_mensal * 12) + (despesa_variavel_mensal * 12)
lucro_operacional_anual = receita_anual - (despesa_operacional_anual + depreciacao_anual)

print("Valor anual das despesas operacionais: ", despesa_operacional_anual)
print("Lucro operacional anual: ", lucro_operacional_anual)

# %%
