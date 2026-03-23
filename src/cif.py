import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator


def simular_padrao_drx(caminho_cif):
    """
    Gera um padrão de difração de raios X (XRD) a partir de um arquivo CIF.

    Parâmetros
    ----------
    caminho_cif : str
        Caminho para o arquivo .cif

    Retorna
    -------
    dois_theta : numpy.ndarray
        Ângulos 2θ (graus)
    intensidade_norm : numpy.ndarray
        Intensidades normalizadas (0 a 1)
    """

    # carregar estrutura cristalina
    estrutura = Structure.from_file(caminho_cif)

    # calcular padrão de DRX
    calculador = XRDCalculator(wavelength="CuKa")
    padrao = calculador.get_pattern(estrutura)

    # normalizar intensidades
    intensidade_norm = padrao.y / np.max(padrao.y)

    return padrao.x, intensidade_norm