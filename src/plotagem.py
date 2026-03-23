import matplotlib.pyplot as plt
import numpy as np
import os

def plotar_xrd(
    dois_theta_exp,
    intensidade_norm_exp,
    padroes_cif,
    nome_arquivo_exp,
    caminho_saida
):
    """
    Plota difração experimental comparada com múltiplos CIFs
    em um único gráfico.
    """

    if not padroes_cif:
        raise ValueError("Nenhum padrão CIF foi fornecido.")

    # cores fixas (melhor para controle visual)
    cores = ["red", "blue", "green", "purple", "orange", "brown"]

    plt.figure(figsize=(10, 5))

    # experimental
    plt.plot(
        dois_theta_exp,
        intensidade_norm_exp,
        color="black",
        linewidth=1.5,
        label="Experimental"
    )

    # CIFs
    for (nome_arquivo, (tt, intensidade)), cor in zip(
        padroes_cif.items(),
        cores
    ):
        nome_legenda = os.path.basename(nome_arquivo)

        plt.vlines(
            tt,
            0,
            intensidade,
            color=cor,
            label=nome_legenda,
            alpha=0.7
        )

    plt.xlim(10, 70)
    plt.ylabel("Intensidade")
    plt.xlabel("2θ (graus)")
    plt.yticks([])
    plt.xticks(np.arange(10, 71, 5))
    plt.legend()
    plt.grid(alpha=0.2)

    plt.title(f"Comparação Experimental vs CIFs\nArquivo: {nome_arquivo_exp}")

    # salvar
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()