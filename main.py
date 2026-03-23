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
import os
from src.cif import simular_padrao_drx

# caminho do arquivo experimental
arquivo_exp = "data/SrTiO3-exemplo.TXT"

# carregar dados
dois_theta_exp, intensidade_exp = carregar_experimental(arquivo_exp)

# normalizar
intensidade_norm_exp = normalizar_intensidade(intensidade_exp)

#Colocar os nomes dos cifs a serem testados.
arquivos_selecionados = [
    "CIF-SrTiO3.cif",
   
]

padroes_cif = {}


for arquivo in arquivos_selecionados:
    caminho = os.path.join("data/cifs", arquivo)

    dois_theta, intensidade = simular_padrao_drx(caminho)

    padroes_cif[arquivo] = (dois_theta, intensidade)

# gerar gráfico
plotar_xrd(
    dois_theta_exp,
    intensidade_norm_exp,
    padroes_cif,
    arquivo_exp,
    "saidas/resultado.png"
)
