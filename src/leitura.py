import pandas as pd

def carregar_experimental(caminho_arquivo):
    """
    Carrega um arquivo experimental de difração de raios X (.txt).

    O arquivo deve conter duas colunas:
    - two_theta (2θ em graus)
    - intensidade

    Parâmetros
    ----------
    caminho_arquivo : str
        Caminho para o arquivo experimental.

    Retorna
    -------
    dois_theta : numpy.ndarray
        Valores de 2θ (graus).
    intensidade : numpy.ndarray
        Intensidades correspondentes.
    """

    dados = pd.read_csv(
        caminho_arquivo,
        sep="\t",
        skiprows=2,
        names=["two_theta", "intensidade"]
    )

    dois_theta = dados["two_theta"].values
    intensidade = dados["intensidade"].values

    return dois_theta, intensidade
