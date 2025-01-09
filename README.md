# Projeto de Redução de Dimensionalidade de Imagens

Este projeto consiste na transformação de uma imagem colorida em duas versões: uma em tons de cinza e outra binária (preto e branco). Ele permite que o usuário faça o upload de uma imagem, realize as transformações e faça o download das imagens resultantes. O projeto foi desenvolvido em Python e inclui a utilização de bibliotecas como `PIL`, `matplotlib`, `numpy`, e `tkinter` para criação de interfaces gráficas (local) e manipulação de imagens.

### Conceito:

A redução de dimensão no espaço de cor é uma das técnicas essenciais para otimizar o processamento de imagens em Machine Learning. Ao simplificar as representações das imagens, como a conversão para tons de cinza ou binário, é possível melhorar a eficiência computacional e reduzir o risco de overfitting nos modelos de aprendizado de máquina.

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

### Exemplo de execução passo a passo
1. Ao executar o script, uma janela será exibida para que você realize o upload de uma imagem
    ![image](https://github.com/user-attachments/assets/077065a4-bb8a-4d8b-9337-11e8ddd5c146)

2. Ao selecionar a imagem, ela será exibida colorida, depois em tons de cinza, e por último, em preto e branco
   ![image](https://github.com/user-attachments/assets/1a63a6c5-a984-4b2a-b83f-8811f232e10e)
   ![image](https://github.com/user-attachments/assets/2ee4ab49-cdb9-4561-9008-ab6c6bcacf41)
   ![image](https://github.com/user-attachments/assets/3c3f9df8-1d4a-4efa-9a66-62a6e13c1ff3)

3. Por último, você pode realizar salvar as fotos geradas, se quiser. Elas serão salvas na pasta `/images`
   ![image](https://github.com/user-attachments/assets/b353a71a-e200-4e03-a0f0-54a0d54e324e)

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
