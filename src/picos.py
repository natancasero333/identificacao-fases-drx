import numpy as np

def normalizar_intensidade(intensidade):
    """
    Normaliza a intensidade dividindo pelo valor máximo.

    Retorna
    -------
    intensidade_norm : numpy.ndarray
        Intensidade normalizada (0 a 1).
    """

    intensidade_norm = intensidade / np.max(intensidade)
    return intensidade_norm
