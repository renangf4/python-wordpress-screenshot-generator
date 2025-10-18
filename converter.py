import os
from PIL import Image

input_dir = "imagens"
output_dir = "convertidos_png"

# Dimensões finais desejadas
LARGURA_FINAL = 1200
ALTURA_FINAL = 600

# Tolerância para achatar (10%)
TOLERANCIA_ALTURA = 0.1

os.makedirs(output_dir, exist_ok=True)

extensoes_validas = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")

for nome_arquivo in os.listdir(input_dir):
    if nome_arquivo.lower().endswith(extensoes_validas):
        caminho_entrada = os.path.join(input_dir, nome_arquivo)
        nome_base = os.path.splitext(nome_arquivo)[0]
        caminho_saida = os.path.join(output_dir, "screenshot.png")

        try:
            # Abrir a imagem
            img = Image.open(caminho_entrada)
            
            # Converter para RGB se necessário
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Calcular nova altura mantendo proporção para largura 1200
            largura_original, altura_original = img.size
            proporcao = LARGURA_FINAL / largura_original
            nova_altura = int(altura_original * proporcao)
            
            # Redimensionar para largura 1200
            img_redimensionada = img.resize((LARGURA_FINAL, nova_altura), Image.Resampling.LANCZOS)
            
            # Verificar se a diferença de altura é pequena (dentro da tolerância)
            diferenca_altura = abs(nova_altura - ALTURA_FINAL) / ALTURA_FINAL
            
            if diferenca_altura <= TOLERANCIA_ALTURA:
                # Achatar para 1200x600
                img_final = img_redimensionada.resize((LARGURA_FINAL, ALTURA_FINAL), Image.Resampling.LANCZOS)
                print(f"Convertido (achatado): {nome_arquivo} -> screenshot.png")
            else:
                # Recortar do topo para 1200x600
                if nova_altura > ALTURA_FINAL:
                    # Recortar do topo (começando em y=0)
                    img_final = img_redimensionada.crop((0, 0, LARGURA_FINAL, ALTURA_FINAL))
                    print(f"Convertido (recortado do topo): {nome_arquivo} -> screenshot.png")
                else:
                    # Se a altura for menor, achata mesmo assim
                    img_final = img_redimensionada.resize((LARGURA_FINAL, ALTURA_FINAL), Image.Resampling.LANCZOS)
                    print(f"Convertido (achatado): {nome_arquivo} -> screenshot.png")
            
            # Quantizar cores para reduzir tamanho (256 cores é suficiente para web)
            img_final = img_final.quantize(colors=256, method=2)
            
            # Salvar com compressão máxima otimizada para WordPress
            img_final.save(caminho_saida, 'PNG', optimize=True, compress_level=9)

        except Exception as e:
            print(f"Erro ao converter {nome_arquivo}: {e}")
