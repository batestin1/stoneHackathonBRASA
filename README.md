<h1 align="center">
<img src="https://img.shields.io/static/v1?label=Hackathon%20BRASA%20POR&message=MAYCON%20BATESTIN&color=7159c1&style=flat-square&logo=ghost"/>


<h3> <p align="center">Hackathon BRASA </p> </h3>
<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

1. Este repositório refere-se ao projeto do Hackathon BRASA, case da STONE 

>> <h3> Problema </h3>

1. Encontrar soluções da STONE para gerenciar negócio (pagamentos, vendas, conta bancária).
Busca oferecer uma experiência memorável aos seus clientes.
2. Criar um sistema de recomendação com base nas transações de máquinas STONE
3. Ajudar a prever quais categorias de compras um cliente pode realizar de acordo com suas transações.
4. Oferecer cross-selling baseado nas compras.

>> <h3> Solução </h3>

1. Uso de um sistema de recomendação baseado no algoritimo NearestNeighbors


>> <h3> Origem dos dados </h3>

1. [LINK](https://drive.google.com/open?id=1RhBcilf-PuP4Zj1XsYmhN1sV_yk2kVQK&usp=drive_fs)

>> <h3> Desenvolvedores </h3>

1. Cristiane Rodrigues da Silva
2. Fernando Rodrigues da Silva
3. Maycon Cypriano Batestin


>> <h3> Árvore do Projeto </h3>

Resumo do diretório 'sistema_recomendacao':
Total de pastas: 4
Total de arquivos: 13

- **`dataset`**: pasta dos conteúdos dos dados.
  - **`dados_consolidados.csv`**: Dados consolidados dos parquets originais.
  - **`hackathon_stone_brasa_sales_data.parquet`**: Dados relacionados ao hackathon.
  - **`hackathon_stone_brasa_banking_data.parquet`**: Dados relacionados ao hackathon.
  - **`mcc.parquet`**: Dados de MCC (Merchant Category Code).

- **`graphs`**: pasta dos conteúdos dos graficos.
  - **`heatmap_descricao.png`**: Arquivo em png sobre heatmap.
  - **`pagamentos_por_regiao.png`**: Arquivo em png sobre relação entre pagamentos e região.
  - **`valor_region.png`**: Arquivo em png sobre relação entre o valor e os estados.
  - **`valor_tempo.png`**: Arquivo em png sobre a questão de valores e data de coleta.

- **`models`**: pasta dos conteúdos dos modelos de IA.
  - **`encoder_recomendacao.pkl`**: Arquivo em pkl para encodar dados categóricos.
  - **`modelo_recomedacao.pkl`**: Arquivo em pkl para aplicar sistema de recomendação.
  
- **`script`**: pasta dos conteúdos de scripts.
  - **`cross_selling_stones_hackthon.ipynb`**: Arquivo em notação jupyter contendo analises e aplicação de Machine Learning.
  - **`cross_selling_stones_hackthon.py`**: Arquivo em python contendo o machine learning e o modelo de sistema de recomendação.
