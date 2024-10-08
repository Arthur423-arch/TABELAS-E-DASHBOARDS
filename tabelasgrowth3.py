import streamlit as st
import pandas as pd

# Função para criar a tabela de vendas
def criar_tabela_vendas(df):
    # Filtrar os dados para a tabela de vendas
    tabela_vendas = df[df['A/V'] == 'Venda'].copy()
    tabela_vendas['Valor Total da Venda'] = tabela_vendas['Valor de Entrada']  # Aqui você pode ajustar o cálculo conforme necessário
    return tabela_vendas

# Função para criar a tabela de aluguel
def criar_tabela_aluguel(df):
    # Filtrar os dados para a tabela de aluguel
    tabela_aluguel = df[df['A/V'] == 'Aluguel'].copy()
    tabela_aluguel['Valor Total do Aluguel'] = tabela_aluguel['Caução'] * 4  # Exemplo: Valor total do aluguel pode ser baseado na caução (ajuste conforme necessário)
    return tabela_aluguel

# Configuração do Streamlit
st.title("Reestruturação da Área de Growth da Mottu")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(uploaded_file)

    # Exibir os dados do CSV
    st.subheader("Dados Carregados")
    st.dataframe(df)

    # Verifica se as colunas necessárias estão presentes
    if all(col in df.columns for col in ['Data', 'A/V', 'Estado', 'Valor de Entrada', 'Caução']):
        # Criar e exibir a tabela de vendas
        tabela_vendas = criar_tabela_vendas(df)
        st.subheader("Tabela de Vendas")
        st.dataframe(tabela_vendas)

        # Criar e exibir a tabela de aluguel
        tabela_aluguel = criar_tabela_aluguel(df)
        st.subheader("Tabela de Aluguel")
        st.dataframe(tabela_aluguel)
    else:
        st.error("O arquivo CSV deve conter as colunas: 'Data', 'A/V', 'Estado', 'Valor de Entrada', 'Caução'.")
