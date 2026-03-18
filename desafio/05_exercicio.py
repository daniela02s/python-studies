# %% 

dados_vendas = {
    "janeiro": 12000.0,
    "fevereiro": 15000.0,
    "março": 13000.0,
    "abril": 14000.0,
    "maio": 16000.0
}

junho = {"junho": 17000.0}
dados_vendas.update(junho)
print(dados_vendas)

total_anual = sum(dados_vendas.values())

mes_maior_venda = max(dados_vendas, key=dados_vendas.get)
print("Mês com maior venda: ", mes_maior_venda)
mes_menor_venda = min(dados_vendas, key=dados_vendas.get)
print("Mês com menor venda: ", mes_menor_venda)

print(dados_vendas.keys)  

meses = list(dados_vendas.keys())
print(meses)
valores = list(dados_vendas.values())
print(valores)

# %%
