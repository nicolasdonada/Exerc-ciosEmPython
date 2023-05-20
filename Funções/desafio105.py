def notas(*nums, sit=0):
    dados = {}

    dados["Total"] = len(nums)
    dados["Maior"] = max(nums)
    dados["Menor"] = min(nums)
    dados["Média"] = sum(nums) / len(nums)

    if sit:
        if dados["Média"] > 9:
            dados["Situação"] = "Ótima"
        if dados["Média"] >= 6 and dados["Média"] < 9:
            dados["Situação"] = "Boa"
        if dados["Média"] < 5:
            dados["Situação"] = "Ruim"

    return dados

resp = notas(10,8,4,2,6, sit=True)

print(resp)