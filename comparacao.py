import numpy as np

def comparar_padroes(picos_exp, intens_exp, x_teorico, y_teorico, tolerancia=0.6):
    """
    Calcula similaridade entre padrão experimental e teórico.
    """

    score = 0
    peso_total = 0

    for p_exp, i_exp in zip(picos_exp, intens_exp):

        peso_total += i_exp

        diferencas = np.abs(x_teorico - p_exp)
        idx = np.argmin(diferencas)

        delta = diferencas[idx]

        if delta < tolerancia:

            i_teo = y_teorico[idx]

            peso_pos = 1 - delta / tolerancia
            peso_int = 1 - abs(i_exp - i_teo)

            score += peso_pos * peso_int * i_exp

    if peso_total > 0:
        score /= peso_total

    return score