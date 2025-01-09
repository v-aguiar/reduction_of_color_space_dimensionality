# Projeto de Redução de Dimensionalidade de Imagens

Este projeto consiste na transformação de uma imagem colorida em duas versões: uma em tons de cinza e outra binária (preto e branco). Ele permite que o usuário faça o upload de uma imagem, realize as transformações e faça o download das imagens resultantes. O projeto foi desenvolvido em Python e inclui a utilização de bibliotecas como `PIL`, `matplotlib`, `numpy`, e `tkinter` para criação de interfaces gráficas (local) e manipulação de imagens.

### Funcionalidades:

- **Upload de imagem**: O usuário pode fazer o upload de uma imagem.
- **Conversão para Tons de Cinza**: A imagem colorida é convertida para tons de cinza utilizando a fórmula RGB para tons de cinza.
- **Conversão para Binário (Preto e Branco)**: A imagem em tons de cinza é convertida em uma imagem binária com base em um valor de limiar.
- **Download das imagens**: O usuário pode baixar tanto a imagem em tons de cinza quanto a imagem binária.

### Requisitos

O projeto depende das seguintes bibliotecas:

- `numpy`
- `matplotlib`
- `PIL` (Pillow)
- `tkinter` (somente para execução local)

No Google Colab, `tkinter` não é necessário, e as imagens são baixadas diretamente com a função `files.download()`.

### Instalação das Bibliotecas Locais

Execute o seguinte comando para instalar as bibliotecas necessárias no seu ambiente local:

```bash
pip install numpy matplotlib pillow
```

### Uso no Google Colab

1. Abra o notebook do Google Colab (link abaixo).
2. Execute as células do notebook.
3. Faça o upload da imagem quando solicitado.
4. As imagens convertidas estarão disponíveis para download ao final da execução.

### Link para o Google Colab

Clique [aqui](https://colab.research.google.com/drive/1cIXxTBc9FmDK1ioxyV4qZSog4KN7pZOs?usp=sharing) para acessar o notebook do Google Colab.

### Como Rodar Localmente

1. Clone este repositório para o seu computador.
2. Instale as dependências necessárias executando `pip install -r requirements.txt`.
3. Execute o script `script.py` para iniciar a interface gráfica e o processo de upload, conversão e download.

### Estrutura do Projeto

O repositório contém a seguinte estrutura de arquivos:

```
/reduction_of_color_space_dimensionality_challenge
    ├── script.py                # Script principal para execução local
    ├── images/                  # Pasta onde as imagens geradas serão salvas (E existe uma imagem colorida de teste + as imagens geradas a partir da mesma)
    ├── requirements.txt         # Arquivo com as dependências necessárias
    └── README.md                # Este arquivo
```

### Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---
