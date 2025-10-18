# Conversor de Imagens para PNG 1200x600 (Python)

Este script converte automaticamente todas as imagens de uma pasta para o formato `.png` com dimensões de 1200x600 pixels, otimizado para upload no WordPress. O script redimensiona, achata ou recorta as imagens conforme necessário.

---

## ✅ Requisitos

- Python 3.x instalado
- Pillow (PIL) - biblioteca de processamento de imagens

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 📁 Estrutura esperada

Crie a seguinte estrutura de pastas:

```
projeto/
├── converter.py              # Script principal em Python
├── requirements.txt          # Dependências Python
├── imagens/                  # Coloque aqui as imagens (.jpg, .png, etc.)
└── convertidos_png/          # Pasta de saída (será criada automaticamente)
    └── screenshot.png        # Imagem convertida 1200x600
```

> ⚠️ **Importante**: Crie a pasta `imagens/` e coloque suas imagens antes de rodar o script.

---

## ▶️ Como usar

1. Instale as dependências com:

```bash
pip install -r requirements.txt
```

2. Coloque suas imagens na pasta `imagens/`
3. Execute o script com:

```bash
python converter.py
```

ou utilize o atalho:

```bash
exec.bat
```

Os arquivos convertidos serão salvos automaticamente como `convertidos_png/screenshot.png`.

---

## 🔧 Como funciona

O script processa as imagens com a seguinte lógica:

1. **Redimensiona** a largura para 1200px mantendo a proporção
2. **Verifica a altura resultante:**
   - Se a diferença para 600px for pequena (≤10%), **achata** a imagem para 1200x600
   - Se a altura for maior que 600px, **recorta do topo** para 1200x600
   - Se a altura for menor, **achata** para 1200x600
3. **Salva** como `screenshot.png` com compressão máxima otimizada para WordPress

### Ajustes (opcional)

Para alterar a tolerância de achatamento, edite a linha:

```python
TOLERANCIA_ALTURA = 0.1  # ← 10% de tolerância
```

---

## 📄 Licença

Este projeto é livre para uso pessoal ou profissional.
