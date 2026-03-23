"""
Script principal para análise de difração de raios X (XRD).

Fluxo:
1. Carrega dados experimentais
2. Normaliza intensidades
3. Compara com padrões CIF
4. Gera gráfico em PDF
"""

from src.leitura import carregar_experimental
from src.processamento import normalizar_intensidade
from src.plotagem import plotar_xrd

# caminho do arquivo experimental
arquivo_exp = "dados/experimental/exp.txt"

# carregar dados
dois_theta_exp, intensidade_exp = carregar_experimental(arquivo_exp)

# normalizar
intensidade_norm_exp = normalizar_intensidade(intensidade_exp)

# definir padrões CIF (exemplo)
if not padroes_cif:
    raise ValueError("Defina o dicionário 'padroes_cif' com os padrões CIF.")

# gerar gráfico
plotar_xrd(
    dois_theta_exp,
    intensidade_norm_exp,
    padroes_cif,
    arquivo_exp,
    "saidas/pdf/resultado.pdf"
)
