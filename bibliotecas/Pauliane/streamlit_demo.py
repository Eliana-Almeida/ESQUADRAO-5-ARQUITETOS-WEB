import streamlit as st
import pandas as pd
st.set_page_config(page_title='Streamlit ao Vivo', page_icon='🚀', layout='centered')
st.title('🚀 Streamlit ao Vivo')
st.write('Streamlit cria dashboards e interfaces interativas usando Python.')
nome = st.text_input('Digite seu nome', 'Pauliane')
dados = pd.DataFrame({'Biblioteca':['Streamlit','Selenium'], 'Função':['Dashboard','Automação'], 'Status':['Funcionando','Funcionando']})
if st.button('Executar demonstração'):
    st.success(f'Olá, {nome}! O Streamlit está funcionando ao vivo.')
st.dataframe(dados, use_container_width=True)
st.bar_chart(pd.DataFrame({'valor':[5,8]}, index=['Dashboard','Automação']))
st.caption('Para voltar ao portal, abra: http://127.0.0.1:5000')
