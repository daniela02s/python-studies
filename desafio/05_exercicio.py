# %% 

receita_trimestral = 800000
custo_produtos = 300000
despesa_operacional = 100000
despesa_financeira = 20000
impostos = 50000
depreciacao = 30000
amortizacao = 10000

lucro_operacional_bruto = receita_trimestral - (custo_produtos + despesa_operacional)
lucro_liquido = lucro_operacional_bruto - (despesa_financeira + impostos)
ebitda_trimestral = lucro_liquido + depreciacao + amortizacao

print("Lucro operacional bruto: ", lucro_operacional_bruto)
print("Lucro líquido: ", lucro_liquido)
print("EBITDA trimestral: ", ebitda_trimestral)

# %%
