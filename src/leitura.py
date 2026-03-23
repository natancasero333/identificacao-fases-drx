import pandas as pd

def carregar_experimental(caminho_arquivo):
    dados = pd.read_csv(
        caminho_arquivo,
        delim_whitespace=True,
        skiprows=12,
        names=["two_theta", "intensidade"]
    )

    dois_theta = dados["two_theta"].values
    intensidade = dados["intensidade"].values

    return dois_theta, intensidade
