import pandas as pd

def carregar_experimental(caminho_arquivo):
    dados = pd.read_csv(
        caminho_arquivo,
        sep=r"\s+",
        skiprows=12,
        names=["two_theta", "intensidade"]
    )

    # forçar conversão para número
    dados["two_theta"] = pd.to_numeric(dados["two_theta"], errors="coerce")
    dados["intensidade"] = pd.to_numeric(dados["intensidade"], errors="coerce")

    # remove qualquer linha que não seja número válido
    dados = dados.dropna()

    dois_theta = dados["two_theta"].values
    intensidade = dados["intensidade"].values

    return dois_theta, intensidade
