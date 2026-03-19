import pandas as pd

def carregar_dados_experimentais(caminho_arquivo):
    """
    Carrega dados de DRX experimental.

    Retorna:
    two_theta, intensidade
    """
    dados = pd.read_csv(
        caminho_arquivo,
        sep="\t",
        skiprows=2,
        names=["two_theta", "intensidade"]
    )

    return dados["two_theta"].values, dados["intensidade"].values