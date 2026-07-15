import pandas as pd
import matplotlib.pyplot as plt

funcionarios = r'01 Project_data\CadastroFuncionarios.csv'
clientes = r'01 Project_data\CadastroClientes.csv'
servicos = r'01 Project_data/BaseServi�osPrestados.xlsx'
#peguei o path do arquivo q esta dentro da pasta do arquivo.py, usei o 'r' no começo pra evitar erros 



funcionarios_df = pd.read_csv(funcionarios, sep=';', decimal=',')
clientes_df = pd.read_csv(clientes, sep=';', decimal=',')
#li o arquivo em csv pq o arquivo é arquivo.csv, usei a separação normal e a decimal pq arquivos com valores em excel geralmente tem decimais
servicos_df = pd.read_excel(servicos)
#li o arquivo em xlsx em excel q n precisa de sep
print("\n" + "="*60 + "\n")
print(servicos_df)
print("\n" + "="*60 + "\n")
print(clientes_df)
print("\n" + "="*60 + "\n")
print(funcionarios_df)
#print de todos para ver as informações caso necessario 

print("\n" + "="*60 + "\n")

### --- 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?
#  Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários ---
    
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
#utilizei o drop para retirar as colunas inuteis da minha tabela, utilizei o axis=1 pra percorrer horizontalmente

gasto_funcionario = funcionarios_df[['Salario Base','Impostos','Beneficios','VT','VR']].sum(axis=1)
#Peguei todas colunas de valores e somei elas em linhas com o axis=1, se eu não uso ele, o python usa o axis=0 q soma colunas inteiras
total = sum(gasto_funcionario) 
# aqui eu fiz a soma pra ver o montante final do valor q a empresa gasta 

funcionarios_df['TOTAL'] = gasto_funcionario
# Adicionar coluna em Pandas é sempre no formato:
# DataFrame + nome da coluna + valor


print(funcionarios_df[['TOTAL']])
print(f"O montante total foi de: R$ {total:,.2f}")
#Aqui foi utlizado as [[]] pra pegar a tabela inteira porem so o que eu quero dela.
#Aqui da pra ver o valor que cada funcionario recebe

print("\n" + "="*60 + "\n")
    
### -----  2. Qual foi o faturamento da empresa? Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos

faturamento_df = clientes_df.merge(servicos_df, on='ID Cliente')
#aqui uma variavel para armazenar o merge dos dataframes usando o ID Cliente como chave em comum,
#para relacionar corretamente cada serviço ao seu respectivo cliente

faturamento = faturamento_df['Valor Contrato Mensal'] * faturamento_df['Tempo Total de Contrato (Meses)']
#fiz a multiplicação para ter o faturamento

faturamento_df = sum(faturamento)
# fiz a soma para obter um valor unico de faturamento

print(f'o faturamento foi de {faturamento_df :,.2f}')
#print do faturamento formatado para aparecer os decimais. 

print("\n" + "="*60 + "\n") 

###  ---- 3. Qual o % de funcionários que já fechou algum contrato?
#     Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>
#     . Na base de funcionários temos uma lista com todos os funcionários<br>
#     . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>
#     . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>
#     Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>
#     Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 


taxa_fechamento = len(servicos_df['ID Funcionário'].unique()) / len(funcionarios_df['ID Funcionário'].unique())
#aqui eu criei uma variavel para armazenar a taxa de fechamento, vi o numero de quantos fecharam nos servicos e qual era o total de funcionaros nos funcionarios_df, usei unique() para remover duplicatas
print(f"A porcentagem de taxa de fechamento foi de :{taxa_fechamento * 100:.2f}%")
#Fiz a porcentagem e formatei para ter duas casas apos o ponto

print("\n" + "="*60 + "\n")

###  ------- 4. Calcule o total de contratos que cada área da empresa já fechou

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário') 
#criei um dataframe para colocar as informações do merge dentro dela
#o primeiro df sempre recebe as informações de qm ta em (), ou seja, servicos_df vai receber
#as colunas do funcionario_df
#  [serve para selecionarmos a tabela ['serve para pegarmos uma coluna/lista em especifico'] ]
contratos_area_quantidade_df = contratos_area_df['Area'].value_counts()
#usei o value_counts() para contar os valores de uma coluna especifica
# ele da como resposta uma tabela com a informação e a quantidade dela
print(contratos_area_quantidade_df)

print("\n" + "="*60 + "\n")

### --- 5. Calcule o total de funcionários por área

funcionarios_por_area_df = funcionarios_df['Area'].value_counts()
#aqui eu so precisei pegar uma coluna especifica do df q eu precisava e peguei o valor com value.counts()
print(f'A quantidade de funcionarios por area: {funcionarios_por_area_df}')

#print(funcionarios_por_area_df.plot(kind='bar'))
#plt.show()
#quis deixar como grafico e usei o .plot e kind='bar' pra deixar como barra tb

print("\n" + "="*60 + "\n")

###  -------- 6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#     Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

# Obs: Lembrando as opções mais usuais de encoding:<br>
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'

# Observação Importante: Se o seu código der um erro na hora de importar os arquivos:<br>
# - CadastroClientes.csv
# - CadastroFuncionarios.csv

# Use separador ";" (ponto e vírgula) para resolver e inclua o parâmetro decimal ',' para o pandas identificar os números corretamente

media_mensal_contratual = clientes_df['Valor Contrato Mensal'].mean()
print(f'A media mensal contratual é de: {media_mensal_contratual :,.2f}')
