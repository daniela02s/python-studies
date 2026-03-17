# %%

cliente = {
    "nome": "Ana",
    "idade": 30,
    "renda_mensal": 4000,
    "emprestimos_anteriores": 1,
    "status_vip": False
}

nome = cliente["nome"]
renda = cliente["renda_mensal"]
emprestimos = cliente["emprestimos_anteriores"]
vip = cliente["status_vip"]

condicao1 = (renda >= 3000) and (emprestimos == 0)
condicao2 = vip == True

aprovado_credito = condicao1 or condicao2

print("Ana tem direito a empréstimo?", aprovado_credito)

# %%
