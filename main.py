import os
import matplotlib.pyplot as plt

from src.leitura import carregar_dados_experimentais
from src.picos import detectar_picos, normalizar_intensidade
from src.drx import simular_padrao_drx
from src.comparacao import comparar_padroes

# =========================
# Configurações
# =========================

arquivo_experimental = "data/experimental.txt"
pasta_cifs = "data/cifs"

# =========================
# Carregar dados
# =========================

two_theta, intensidade = carregar_dados_experimentais(arquivo_experimental)

intensidade_norm = normalizar_intensidade(intensidade)

# =========================
# Detectar picos
# =========================

indices, picos_exp, intens_exp = detectar_picos(two_theta, intensidade)

# =========================
# Comparar com CIFs
# =========================

resultados = []

for arquivo in os.listdir(pasta_cifs):

    if arquivo.endswith(".cif"):

        caminho = os.path.join(pasta_cifs, arquivo)

        try:
            x_teo, y_teo = simular_padrao_drx(caminho)

            score = comparar_padroes(
                picos_exp,
                intens_exp,
                x_teo,
                y_teo
            )

            resultados.append((arquivo, score))

        except:
            pass

# ordenar resultados
resultados.sort(key=lambda x: x[1], reverse=True)

print("\nFases mais prováveis:\n")

for r in resultados[:10]:
    print(f"{r[0]} → score = {r[1]:.3f}")

# =========================
# Plot
# =========================

plt.figure(figsize=(10,5))

plt.plot(two_theta, intensidade_norm, color="black", label="Experimental")

for r in resultados[:3]:

    caminho = os.path.join(pasta_cifs, r[0])

    x_teo, y_teo = simular_padrao_drx(caminho)

    plt.vlines(x_teo, 0, y_teo, label=r[0])

plt.xlabel("2θ (graus)")
plt.ylabel("Intensidade normalizada")
plt.title("Comparação DRX")
plt.legend()
plt.xlim(10, 80)

plt.show()