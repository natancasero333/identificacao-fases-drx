import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.cm as cm

def plotar_xrd(
    dois_theta_exp,
    intensidade_norm_exp,
    padroes_cif,
    nome_arquivo_exp,
    caminho_saida
):
    """
    Plota difração experimental comparada com padrões CIF.

    Para cada CIF, é gerado um subplot contendo:
    - curva experimental (linha)
    - picos do CIF (linhas verticais)

    Parâmetros
    ----------
    dois_theta_exp : numpy.ndarray
        Valores de 2θ experimental.
    intensidade_norm_exp : numpy.ndarray
        Intensidade experimental normalizada.
    padroes_cif : dict
        Dicionário no formato:
        {
            "nome_arquivo.cif": (array_two_theta, array_intensidade)
        }
    nome_arquivo_exp : str
        Nome do arquivo experimental (para título).
    caminho_saida : str
        Caminho para salvar o PDF.

    Retorna
    -------
    None
    """

    numero_cifs = len(padroes_cif)
    cores = cm.tab10(np.linspace(0, 1, numero_cifs))

    fig, eixos = plt.subplots(numero_cifs, 1, figsize=(10, 3 * numero_cifs))

    if numero_cifs == 1:
        eixos = [eixos]

    for eixo, (nome_arquivo, (tt, intensidade)), cor in zip(
        eixos,
        padroes_cif.items(),
        cores
    ):
        nome_legenda = os.path.basename(nome_arquivo)

        eixo.plot(
            dois_theta_exp,
            intensidade_norm_exp,
            color="black",
            label="Experimental"
        )

        eixo.vlines(
            tt,
            0,
            intensidade,
            color=cor,
            label=nome_legenda,
            alpha=0.7
        )

        eixo.set_xlim(10, 70)
        eixo.set_ylabel("Intensidade")
        eixo.set_yticks([])
        eixo.set_xticks(np.arange(10, 71, 5))
        eixo.legend()
        eixo.grid(alpha=0.2)

    eixos[-1].set_xlabel("2θ (graus)")

    plt.suptitle(
        f"Comparação Experimental vs CIFs\nArquivo: {nome_arquivo_exp}"
    )

    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()
