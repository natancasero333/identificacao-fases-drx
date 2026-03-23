from src.leitura import carregar_experimental
from src.plotagem import plotar_xrd

arquivo_exp = "dados/experimental/exp.txt"

dois_theta_exp, intensidade_exp = carregar_experimental(arquivo_exp)

plotar_xrd(
    dois_theta_exp,
    intensidade_exp,
    padroes_cif,
    arquivo_exp,
    "saidas/pdf/resultado.pdf"
)
