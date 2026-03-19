import numpy as np
from pymatgen.core import Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator

def simular_padrao_drx(caminho_cif):
    """
    Gera padrão de DRX a partir de um CIF.
    """
    estrutura = Structure.from_file(caminho_cif)

    calculador = XRDCalculator(wavelength="CuKa")

    padrao = calculador.get_pattern(estrutura)

    intensidades = padrao.y / np.max(padrao.y)

    return padrao.x, intensidades