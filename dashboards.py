import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.title("Análise de Faturamento de Filiais de Motos")

# Substituir a parte do uploader pelo caminho direto do arquivo
file_path = './Tabela__-_Case_Mottu_2024.xlsx - Vendas & Aluguel - Dados.csv'

# Ler a planilha diretamente do arquivo existente
data = pd.read_csv(file_path)

# Garantir que as colunas relevantes estão presentes
required_columns = ['Data', 'A/V', 'Estado', 'Valor de Entrada', 'Caução']
if all(col in data.columns for col in required_columns):
    # Calcular faturamento total para cada filial
    faturamento = data.groupby('Estado').agg(
        Faturamento_Total=('Valor de Entrada', 'sum')
    ).reset_index()

    # Ordenar as filiais por faturamento total
    faturamento = faturamento.sort_values(by='Faturamento_Total', ascending=False)

    # Criar um gráfico de barras para o faturamento total por filial
    st.subheader("Faturamento Total por Filial")
    bar_fig = px.bar(faturamento, x='Estado', y='Faturamento_Total',
                     title='Faturamento Total por Filial',
                     labels={'Faturamento_Total': 'Faturamento Total (R$)', 'Estado': 'Filial (Estado)'},
                     color='Faturamento_Total',
                     color_continuous_scale=px.colors.sequential.Viridis)
    st.plotly_chart(bar_fig)

    # Exibir a filial com maior faturamento
    maior_faturamento = faturamento.iloc[0]
    st.subheader("Filial com Maior Faturamento")
    st.write(f"**Estado:** {maior_faturamento['Estado']}")
    st.write(f"**Faturamento Total:** R$ {maior_faturamento['Faturamento_Total']:.2f}")

    # Criar um gráfico de pizza para mostrar a participação do faturamento
    st.subheader("Participação de Faturamento por Filial")
    pie_fig = px.pie(faturamento, values='Faturamento_Total', names='Estado',
                     title='Participação de Faturamento por Filial',
                     color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(pie_fig)

    # Adicionar análise adicional se necessário
    st.subheader("Análise de Fatores Influentes")
    st.write(
        "O desempenho pode ser influenciado por fatores como localização, oferta de motos e qualidade do atendimento."
    )
else:
    st.error("A planilha não contém todas as colunas necessárias.")
