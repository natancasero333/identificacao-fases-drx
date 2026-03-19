import numpy as np
from scipy.signal import find_peaks

def normalizar_intensidade(intensidade):
    """
    Normaliza intensidade para o intervalo [0,1]
    """
    max_val = np.max(intensidade)
    if max_val == 0:
        return intensidade
    return intensidade / max_val


def detectar_picos(two_theta, intensidade, altura_relativa=0.3, distancia=5):
    """
    Detecta picos no difratograma.
    """
    intensidade_norm = normalizar_intensidade(intensidade)

    indices, _ = find_peaks(
        intensidade_norm,
        height=altura_relativa,
        distance=distancia
    )

    posicoes = two_theta[indices]
    intensidades = intensidade_norm[indices]

    return indices, posicoes, intensidades
