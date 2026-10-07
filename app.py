import streamlit as st

# Crie um aplicativo simples com Streamlit que tenha: Um campo de texto para
# digitar o nome de um usuário; Um campo de texto para digitar a função dele (ex:
# “Professor”, “Aluno”); Um botão “Salvar” que mostre uma mensagem de sucesso
# quando clicado. Dica: use st.text_input() e st.button().

# def salvar_usuario():
#     nome = st.selectbox('Selecione o nome do usuário: ', ['Bruna', 'Lucia', 'Lopes']);
#     funcao = st.text_input('Digite o função do usuário: ');
#     if st.button('Salvar'):
#         st.success(f'Usuário {nome} com função {funcao} salvo com sucesso!');

# salvar_usuario();

# -=====-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Crie um aplicativo web simples usando o Streamlit que sirva como uma página de 
# boas-vindas estruturada, utilizando conceitos básicos de exibição de texto e 
# layout. Passo a Passo: 
# Crie um novo arquivo Python chamado boas_vindas.py. 
# Importe a biblioteca do Streamlit (import streamlit as st). Adicione um título 
# principal na página utilizando st.title(). Insira um cabeçalho de seção logo 
# abaixo usando st.header() (ex: "Sobre este App"). Escreva um parágrafo 
# explicativo sobre o objetivo da aula utilizando st.write(). Adicione um divisor 
# horizontal utilizando st.divider() para separar o conteúdo visualmente.

# def app():
#     st.title('Bem-vindo(a) ao App!')
#     st.header('Sobre este App')
#     st.write('O objetivo da aula é criar interface interativa e entender a biblioteca Streamlit.')
#     st.divider()

# app()


# -=====-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# st.title('Hello Word!');
# st.write('Curso do mundo!');

# st.header('Tabela num sei do que');
# st.subheader('Ainda vou descobrir');
# st.text('É só pata teste');
# st.markdown('06/10/26');

# data = {
#     'Nome': ['Bruna', 'Lucia', 'Lopes'],
#     'Idade': [20,30,34],
#     'Salário': [500, 600, 1000]
# };

# df = pd.DataFrame(data);
# st.dataframe(df);
# st.table(df);

# fig, ax = plt.subplots();
# ax.bar(df['Nome'], df['Salário']);
# ax.set_ylabel('Salário')
# st.pyplot(fig);

# # fig, ax = plt.subplots();
# # ax.bar(df['Nome'], df['salário']);
# # ax.set_ylabel('Salário');
# # st.pyplot(fig);

# if st.button('Clique Aqui'):
#     st.write('Botão clicado vez!')

# idade= st.slider('Selecione sua idade', 0, 100, 25)
# st.write(f'Idade selecionada: {idade}')

# opcao = st.selectbox('Selecione uma opção', ['Opção 1', 'Opção 2', 'Opção 3'])
# st.write(f'Opção selecionada: {opcao}')
