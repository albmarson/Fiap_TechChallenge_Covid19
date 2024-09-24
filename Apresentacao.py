import streamlit as st
import pandas as pd
from PIL import Image


# Configurações iniciais
st.set_page_config(page_title="COVID-19", page_icon=":book:", layout="wide")

# Função para mostrar o Propósito
def show_propósito():
    # Título principal
    st.markdown('<h1 style="text-align: center;">O Comportamento dos Brasileiros Durante a Crise de COVID-19</h1>', unsafe_allow_html=True)
    
    # Subtítulo
    st.markdown('<h5 style="text-align: center; font-style: italic;">Impactos Sociais e Comportamentais na Pandemia</h5><br>', unsafe_allow_html=True)

    # Créditos
    st.markdown("""
    <div style="font-size: 12px; text-align: right; max-width: 490px; margin-left: auto; display: block;">
        Elaborado por Alberto M. Marques Marson, Técnico em Informática, Analista e Desenvolvedor de Sistemas, atualmente cursando pós-graduação em Data Analytics.<br><br>
    </div>
    """, unsafe_allow_html=True)

    # Descrição do estudo
    st.markdown('''
    <div style="display: flex; justify-content: center; align-items: center; margin: 0 auto;">
        <div style="border-left: 5px solid white; height: 100%; padding-left: 20px; text-align: justify;">
            O presente estudo, proposto pela FIAP como parte do projeto de conclusão do terceiro trimestre do curso de pós-graduação em Data Analytics, visa analisar o comportamento da população durante a pandemia da COVID-19. A pesquisa tem como objetivo compreender os padrões de contágio e os impactos sociais da doença, a fim de fornecer subsídios para o planejamento de estratégias eficazes em caso de novos surtos. 
        </div>
    </div><br>
    ''', unsafe_allow_html=True)

    # Carregar e exibir a imagem
    imagem = "Img/Banner_Analise.png"
    try:
        img = Image.open(imagem)
        st.image(img, caption="", use_column_width=True)
    except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

# Chame a função para mostrar o Propósito
show_propósito()

# Seções do conteúdo
st.header("Introdução")

st.markdown("""
Antes de adentrar em qualquer análise, é crucial compreender profundamente o tema em questão, explorando suas nuances e contextos específicos. Esta abordagem não apenas estabelece uma base sólida de entendimento, mas também possibilita uma interpretação mais informada e precisa dos dados, além de facilitar a formulação de hipóteses.

Em 2020, o mundo foi abalado por uma crise de saúde pública sem precedentes, causada pelo vírus **SARS-CoV-2**, amplamente conhecido como COVID-19. ***No Brasil, os primeiros casos foram identificados em março e abril de 2020, marcando o início de um período desafiador para a nação***. 

O impacto da pandemia no Brasil foi significativo e multifacetado. A rápida propagação do vírus gerou uma sobrecarga no sistema de saúde, com hospitais enfrentando dificuldades para lidar com o aumento de pacientes. As medidas de contenção, como o distanciamento social, o uso de máscaras e o fechamento temporário de negócios, foram implementadas em um esforço para limitar a disseminação do vírus. Essas ações, embora essenciais, tiveram profundas implicações econômicas e sociais.

Em termos de mortalidade, o Brasil foi um dos países mais afetados pela pandemia de COVID-19. Até hoje, o país registrou um total de **713.177 óbitos**. O número alarmante de mortes inicialmente começou a crescer de forma acentuada em 2020 e continuou a aumentar nos meses subsequentes. Essa alta taxa de mortalidade refletiu uma combinação de fatores complexos, incluindo a capacidade limitada do sistema de saúde para lidar com a demanda crescente e a dificuldade de gerenciar a pandemia em um país com profundas desigualdades regionais e socioeconômicas.

A vacinação contra a COVID-19 começou no Brasil em janeiro de 2021, com a implementação de campanhas de imunização massiva. A vacinação desempenhou um papel crucial na redução da taxa de infecção e mortalidade, contribuindo para a desaceleração da pandemia. O progresso foi notável, com milhões de brasileiros recebendo a vacina e, eventualmente, levando a uma diminuição significativa nos casos graves e mortes.

No entanto, a pandemia revelou desafios persistentes, incluindo a necessidade urgente de assegurar a equidade na distribuição das vacinas, a adaptação às novas variantes do vírus e a preparação para enfrentar futuras crises de saúde pública. Estes desafios sublinham a importância de uma estratégia abrangente e inclusiva para garantir que todos os segmentos da população recebam proteção adequada e que o sistema de saúde esteja preparado para responder a novas ameaças de forma eficaz.

""")

st.header("Extração dos Dados")

st.markdown("""
A extração de dados para este estudo foi realizada a partir da base de dados pública da **Pesquisa Nacional por Amostra de Domicílios (PNAD COVID-19)**, disponibilizada pelo **IBGE** e acessada através da plataforma **BigQuery**. Essa ferramenta permitiu o acesso eficiente a grandes volumes de dados, facilitando a consulta e o processamento necessário para as análises subsequentes. Esta base contém informações sobre os impactos da pandemia de COVID-19 nas famílias brasileiras, abrangendo aspectos demográficos, socioeconômicos e de saúde.

O primeiro passo foi a extração dos dados, utilizando uma query **SQL** que incorpora uma série de junções entre tabelas, permitindo o cruzamento de diferentes variáveis. Entre as tabelas cruzadas estão a base de microdados e dicionários de variáveis que descrevem informações como sintomas de saúde, dados demográficos e socioeconômicos, e acesso a serviços de saúde.            
            
**Os períodos filtrados para a análise abrangem os meses de julho, agosto e setembro de 2020**, e essa seleção é fundamentada em vários aspectos críticos do contexto da pandemia no Brasil:

- **Em julho de 2020**, o Brasil estava emergindo de um pico inicial de infecções, e esse mês marcou uma fase de transição crucial. As medidas de contenção e estratégias de resposta estavam sendo ajustadas após o aumento acentuado de casos e hospitalizações que caracterizaram os meses anteriores. Julho ofereceu um ponto de referência importante para avaliar como as intervenções iniciais estavam impactando as taxas de infecção e a capacidade do sistema de saúde.

- **Em agosto de 2020**, foi um período de intensificação das estratégias de controle e resposta à pandemia. As políticas de saúde pública foram reavaliadas e ajustadas com base nas informações acumuladas e nos desafios emergentes. Esse mês representou uma fase de adaptação e reforço das medidas de mitigação, tornando-o crucial para examinar a eficácia das novas abordagens e a resposta do sistema de saúde frente ao aumento contínuo de casos.                                              

- **Em setembro de 2020**, começou a mostrar sinais de estabilização, refletindo os efeitos das intervenções e ajustes realizados nos meses anteriores. Esse período permitiu uma avaliação inicial das tendências de desaceleração da pandemia e das mudanças nas dinâmicas de infecção. Analisar setembro é essencial para entender a transição de uma fase crítica para uma relativa estabilização, proporcionando insights sobre a eficácia das políticas a longo prazo e as áreas que ainda precisavam de atenção.
""")

st.header("Preparação dos Dados")

st.markdown("""
Durante o processo de preparação dos dados, foi essencial realizar algumas transformações para garantir a qualidade e a consistência dos dados. Por exemplo, a coluna que contém o nome dos estados foi normalizada para remover acentuações, o que facilita a manipulação e análise dos dados posteriormente. Isso foi feito utilizando a função **TRANSLATE**, que converteu os caracteres acentuados para suas versões sem acento.

Além disso, para o campo de sintomas, foi feita uma agregação que condensa a informação em variáveis indicativas de sintomas relacionados à COVID-19, como febre, tosse, dor de garganta, entre outros. A criação da coluna **teve_sintomas** resume esses dados binariamente, indicando se o indivíduo apresentou algum dos sintomas listados. Outra coluna, **num_sintomas**, contabiliza a quantidade de sintomas reportados, o que permite uma análise mais refinada da severidade dos casos reportados.            

Os dados também englobam informações sobre o atendimento médico recebido, onde são categorizados os diferentes tipos de assistência procurados, como unidades básicas de saúde (UBS), hospitais públicos e privados, além de outros serviços médicos. A coluna **forma_atendimento** foi criada para identificar se o indivíduo buscou assistência hospitalar, outros tipos de atendimento ou se não procurou ajuda médica.            

No aspecto financeiro, foram extraídos dados sobre a renda familiar, aposentadorias, pensões, benefícios sociais e outros rendimentos. A soma de todas essas fontes de rendimento foi calculada e agrupada na coluna **soma_rendimentos**. Isso proporciona uma visão consolidada do impacto econômico sofrido pelas famílias durante a pandemia.            

Esse processo de extração e transformação de dados foi essencial para construir uma base sólida, capaz de viabilizar uma análise aprofundada dos impactos da COVID-19 na saúde, no sistema de atendimento médico e na situação socioeconômica da população brasileira. Essas variáveis são cruciais para compreender como a pandemia afetou diferentes aspectos da vida dos brasileiros, permitindo uma exploração mais detalhada e precisa dos dados nas fases subsequentes. O script utilizado para a extração está disponível no repositório e pode ser encontrado sob o nome: **ExtracaoDadosBaseCovid_BigQuery.sql**.                     
""")

st.header("Análise Interativa de Dados")

# URL do relatório do Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYWFjMjVlM2MtYjQyMS00YTZmLWI1YjktYWFiMzUzMzI3NWY1IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"

# Centralizando o iframe do Power BI
st.markdown(
    f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url}' width='1000' height='500' frameborder='0' allowFullScreen='true'></iframe></div>",
    unsafe_allow_html=True
)

st.markdown("""

O dashboard apresentado acima oferece uma análise interativa dos dados, permitindo que os usuários explorem informações de forma dinâmica e visual. Com a crescente complexidade dos desafios enfrentados, especialmente durante períodos de crise, como a pandemia da covid-19, a necessidade de uma compreensão clara e acessível dos dados se tornou crucial.

Através deste dashboard, é possível identificar tendências, padrões e anomalias nos dados, o que proporciona insights valiosos para a tomada de decisões informadas. Os gráficos e visualizações permitem uma interpretação mais intuitiva, facilitando a análise por diferentes segmentos e variáveis.

Contudo, como sempre, é fundamental realizar uma análise introdutória dos dados apresentados. Abaixo, você encontrará uma análise descritiva que destaca pontos importantes, proporcionando um entendimento mais profundo sobre os resultados obtidos. Essa análise busca elucidar contextos e nuances que podem influenciar a interpretação dos dados, permitindo que as informações sejam absorvidas de maneira mais completa e eficaz.            
""")


st.header("Disseminação do Vírus")

st.markdown("""
Com base nos dados coletados durante os meses de julho, agosto e setembro de 2020, foi possível analisar a situação da disseminação da COVID-19 em uma amostra de 1.157.984 participantes. Dentre esses, 1.135.499 pessoas, ou seja, aproximadamente 98,1% dos entrevistados, testaram negativo para o vírus, enquanto 22.485 indivíduos (1,9%) testaram positivo para a SARS-CoV-2. 

""")
            
contagem_resultados = "ContagemDosResultados.csv"

# Lendo o arquivo CSV
df_resultados = pd.read_csv(contagem_resultados)

# Selecionando apenas as colunas desejadas
colunas_desejadas = ['Resultado do Teste', 'Quantidade', 'Porcentagem sobre o total']
df_resultados = df_resultados[colunas_desejadas]

# Removendo o índice
df_resultados.reset_index(drop=True, inplace=True)     

# Exibindo o DataFrame como uma tabela, centralizando os valores
st.dataframe(df_resultados.style.set_properties(**{'text-align': 'center'}), use_container_width=True)

st.markdown("""
Ao analisar os dados por mês, observa-se que a grande maioria dos participantes manteve resultados negativos ao longo do período. Em julho, 378.839 pessoas (32,7%) testaram negativo, o mesmo ocorreu com 378.881 pessoas (32,7%) em agosto e 377.779 (32,6%) em setembro. Isso demonstra uma estabilidade nas taxas de testes negativos ao longo dos três meses.            

Por outro lado, a taxa de positividade apresentou um leve aumento mês a mês. Em julho, 5.327 pessoas (0,5%) testaram positivo, número que subiu para 7.639 (0,7%) em agosto e alcançou 9.519 (0,8%) em setembro. Embora a porcentagem de positivos seja relativamente baixa, o aumento gradual ao longo dos meses indica um crescimento da disseminação do vírus durante esse período.
""")

# Carregar a imagem
imagem_retornos = "Img/Comparativo Mensal.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("Comparativo Mensal")


st.markdown("""
Embora o número de casos negativos supere o de positivos, é essencial analisar a distribuição geográfica dos casos, uma vez que a disseminação do vírus varia significativamente entre os estados. Apesar da estabilidade nos resultados negativos ao longo dos meses, o aumento gradual na taxa de positividade suscita questões sobre os fatores que podem ter influenciado essa tendência.

A análise dos casos positivos de COVID-19 mostra uma discrepância notável entre os estados, com Maranhão (1.740), São Paulo (1.518), Rio de Janeiro (1.421), Ceará (1.210) e Pará (1.111) liderando em infecções. Essa variação pode ser atribuída a diversos fatores, como densidade populacional, mobilidade urbana, acesso a serviços de saúde e políticas de mitigação implementadas em cada local.

No Maranhão, por exemplo, uma infraestrutura de saúde limitada e desafios na disseminação de informações sobre medidas de prevenção podem ter contribuído para o aumento dos casos. Em contraste, São Paulo, um dos estados mais populosos e economicamente dinâmicos do Brasil, enfrenta uma grande circulação de pessoas, facilitando a disseminação do vírus, mesmo com melhores condições de saúde pública em comparação a outros estados.

O Rio de Janeiro e o Ceará também enfrentam desafios específicos, como a alta concentração populacional em áreas urbanas e a movimentação constante de turistas. Já o Pará pode estar lidando com dificuldades relacionadas ao transporte e ao acesso a serviços de saúde, o que pode impactar os números de testagem e tratamento.

Além disso, a variação nas taxas de vacinação e nas campanhas de conscientização em cada estado é um fator importante a ser considerado. Estados que adotaram estratégias de vacinação mais eficazes e campanhas educativas robustas tendem a apresentar números de casos positivos menores.
            
""")
# Carregar a imagem
imagem_retornos = "Img/5EstadosMaisPositivados.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("5EstadosMaisPositivados")

st.markdown("""
Os dados de COVID-19 revelam que estados como Minas Gerais (103.348), São Paulo (101.085), Rio de Janeiro (85.903), Santa Catarina (69.885) e Rio Grande do Sul (66.772) apresentam um elevado número de resultados negativos. No entanto, é imprescindível contextualizar essas informações em relação às altas taxas de casos positivos em São Paulo e Rio de Janeiro.

Minas Gerais se destaca pela quantidade significativa de resultados negativos, o que indica uma implementação eficaz de testagem e estratégias de prevenção. Essa performance pode ser atribuída a políticas públicas robustas, com acesso adequado a serviços de saúde e campanhas de conscientização direcionadas à população.

São Paulo, apesar de também apresentar uma quantidade considerável de resultados negativos, com 101.085, enfrenta uma complexidade adicional devido à sua alta taxa de positividade (1.518 casos). A densidade populacional e a mobilidade urbana intensa contribuem para a disseminação do vírus, demonstrando que, mesmo com uma infraestrutura de saúde mais desenvolvida, a capacidade de controle da pandemia é desafiada pela dinâmica populacional.

O Rio de Janeiro, que reporta 85.903 resultados negativos e 1.421 positivos, ilustra uma situação análoga. A persistente alta taxa de infecções sugere que as medidas de mitigação implementadas não são suficientes para conter a propagação do vírus, agravadas por fatores como a urbanização e o fluxo turístico.

Em contraste, Santa Catarina e Rio Grande do Sul mostram resultados positivos com um número menor de casos positivos e altos índices de negatividade. Isso sugere que essas regiões têm adotado políticas de saúde pública eficazes, com foco na testagem e na prevenção, mesmo sendo menos populosas.

Portanto, enquanto os altos números de resultados negativos refletem um desempenho positivo nas ações de saúde pública, a discrepância observada em estados como São Paulo e Rio de Janeiro ressalta a necessidade de estratégias específicas para cada localidade. A continuidade da vigilância e a adaptação das medidas de prevenção são essenciais para garantir que a taxa de resultados negativos permaneça elevada, mesmo em um cenário de crescente positividade.
""")

# Carregar a imagem
imagem_retornos = "Img/5EstadosMaisNegativados.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("5EstadosMaisNegativados")

st.header("Restrições de Contato")

st.markdown("""
Após analisarmos a disseminação do vírus, um dos fatores mais importantes a considerar é o afastamento social, uma medida que pode reduzir a contaminação. Os dados coletados revelam diferentes comportamentos da população em relação à restrição de contato durante a pandemia de COVID-19. A análise das respostas demonstra uma variação significativa nas atitudes dos indivíduos frente à necessidade de limitar interações sociais. Vejamos:
""")

contagem_restricoes = "ContagemDeRestricoes.csv"
# Lendo o arquivo CSV
df_resultados_restricoes = pd.read_csv(contagem_restricoes)

# Selecionando apenas as colunas desejadas
colunas_desejadas = ['Restrição de Contato', 'Quantidade', 'Porcentagem sobre o total']
df_resultados = df_resultados_restricoes[colunas_desejadas]

# Garantindo que a coluna 'Quantidade' é do tipo string
df_resultados['Quantidade'] = df_resultados['Quantidade'].astype(str)

# Removendo caracteres desnecessários e convertendo para numérico
df_resultados['Quantidade'] = pd.to_numeric(df_resultados['Quantidade'].str.replace('.', '').str.replace(',', '.'), errors='coerce')

# Formatando a coluna 'Quantidade' para ter o ponto como separador decimal
df_resultados['Quantidade'] = df_resultados['Quantidade'].apply(lambda x: f'{x:,.0f}'.replace(',', '.'))

# Removendo o índice
df_resultados.reset_index(drop=True, inplace=True)

# Exibindo o DataFrame como uma tabela, centralizando os valores
st.dataframe(df_resultados.style.set_properties(**{'text-align': 'center'}), use_container_width=True)

st.markdown("""
**- Ficou em casa e só saiu em caso de necessidade básica:**

Quantidade: 499.967\n
Porcentagem sobre o total: 43,18%\n
Este grupo representa a maior parte da amostra, indicando que quase metade da população adotou uma postura cautelosa, nos meses de julho, agosto e setembro de 2020, priorizando a segurança e limitando suas saídas a necessidades essenciais. Esse comportamento pode refletir a preocupação com a saúde e o entendimento da gravidade da pandemia.

**- Reduziu o contato com as pessoas, mas continuou saindo de casa para trabalho ou atividades não essenciais e/ou recebendo visitas:**

Quantidade: 393.638\n
Porcentagem sobre o total: 33,99%\n
Este segundo grupo, que engloba cerca de um terço da população, revela uma abordagem mais flexível em relação às restrições. Embora tenham reduzido as interações, ainda optaram por manter alguma normalidade em suas vidas, saindo para trabalhar e recebendo visitas, o que pode indicar a necessidade de conciliar a vida profissional com as diretrizes de saúde pública.

**- Ficou rigorosamente em casa:**

Quantidade: 231.646\n
Porcentagem sobre o total: 20%\n
Um quinto da população se comprometeu a permanecer em casa de forma rigorosa, o que demonstra uma adesão forte às recomendações de saúde. Esse comportamento pode ser interpretado como uma resposta a um senso de responsabilidade coletiva ou ao medo da infecção.

**- Não fez restrição, levou vida normal como antes da pandemia:**

Quantidade: 26.157\n
Porcentagem sobre o total: 2,26%\n
Apenas uma pequena fração da população manteve um estilo de vida normal, ignorando as restrições. Este comportamento pode ser atribuído a uma variedade de fatores, como descrença na gravidade da situação ou resistência a mudanças na rotina.

- **Ignorado:**

Quantidade: 6.576\n
Porcentagem sobre o total: 0,57%\n
**A porcentagem mínima de respostas ignoradas sugere que a maioria da população se engajou no processo de reflexão e resposta às diretrizes de saúde pública, mesmo que em graus variados.**
""")

st.markdown("""
Ao analisar os dados sobre as restrições de contato durante a pandemia de COVID-19, observamos que, apesar da maioria da população ter adotado medidas de afastamento social, uma pequena fração não fez restrições, levando uma vida normal como antes da pandemia. Com apenas 2,26% da amostra representando essa postura, o total de 26.157 pessoas sinaliza uma resistência significativa às diretrizes de saúde pública.
 """)                          
       

# Carregar a imagem
imagem_retornos = "Img/5EstadosComMenosDistanciamento.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("5EstadosComMenosDistanciamento")

st.markdown("""
Nos cinco estados onde essa resistência foi mais prevalente — Maranhão (2.594), Minas Gerais (2.304), Pará (2.299), São Paulo (2.273) e Rio de Janeiro (1.770) — é evidente que a comunicação sobre os riscos da COVID-19 pode não ter sido eficaz. A elevada quantidade de pessoas que não respeitaram o distanciamento social sugere uma percepção subestimada da gravidade da pandemia.

Adicionalmente, a baixa adesão a restrições pode refletir uma falta de confiança nas orientações governamentais e na capacidade do sistema de saúde em lidar com a crise. Isso ressalta a importância de estratégias de comunicação mais robustas e transparentes, que ajudem a construir um entendimento mais claro sobre os riscos associados ao vírus e a necessidade de manter o afastamento social.
            
Essa resistência pode ser atribuída a diversos fatores, incluindo crenças pessoais ou políticas que minimizam a necessidade de medidas de segurança, além da dificuldade de adaptação a um novo estilo de vida. Nos estados mencionados, é possível que as consequências econômicas e sociais das restrições tenham sido percebidas como mais imediatas do que os riscos à saúde. Essa perspectiva ressalta a complexidade do cenário, e no próximo tópico, exploraremos mais profundamente a realidade financeira que pode estar moldando essas atitudes.
""")                

st.header("Realidade Financeira")

st.markdown("""
Durante a pandemia da covid-19, a taxa de desemprego atingiu níveis alarmantes no Brasil. A taxa média de desemprego no país atingiu 13,5% em 2020, enquanto em 2019 foi de 11,9%. Os efeitos da pandemia da covid-19 sobre o mercado de trabalho provocaram alta recorde de desemprego em 20 estados, de acordo com o IBGE.

Dos registros analisados, 118.938 pessoas apresentaram rendimentos iguais a zero, indicando uma situação de vulnerabilidade extrema. Em contrapartida, 1.028.045 pessoas conseguiram obter rendimentos, embora o cenário de incerteza ainda prevalecesse. Esses números ressaltam os desafios que o Brasil enfrentou na recuperação econômica durante esses meses críticos, com muitos indivíduos lutando para garantir a subsistência em meio a um ambiente de instabilidade.
""") 

# Carregar a imagem
imagem_retornos = "Img/FaixaRendimento.png"
try:
    img = Image.open(imagem_retornos)
    
   
    largura_max = 1000  
    altura_max = 700   
    
    img.thumbnail((largura_max, altura_max))  
    
    
    col1, col2, col3 = st.columns([1, 3, 1])  
    
    with col2:
        st.image(img, caption="", use_column_width=True)  

except FileNotFoundError:
    st.error("Imagem não encontrada. Verifique o caminho para a imagem.")
def show_volatilidade():
    st.header("FaixaRendimento")

st.markdown("""
As faixas de rendimento de 0 a 499 reais e 500 a 999 reais revelam uma realidade alarmante sobre a vulnerabilidade econômica da população brasileira durante a pandemia de covid-19, especialmente considerando que o salário mínimo em 2020 era de R$ 1.039,00.

- **Total na Faixa de 0 a 499 Reais:**

Nesta faixa, 118.938 pessoas estão registradas. Dentre elas, 106.419 pessoas possuem rendimentos iguais a zero reais. Esse dado é preocupante, pois representa quase 90% do total dessa faixa, evidenciando a extrema vulnerabilidade econômica e a luta diária por sobrevivência.

- **Faixa de 500 a 999 Reais:**

A faixa de 500 a 999 reais inclui 123.986 pessoas. Embora essa faixa represente um ligeiro aumento nos rendimentos, ainda está muito abaixo do salário mínimo, o que indica que muitas pessoas estão lutando para atingir um padrão de vida básico.

- **Implicações Sociais:**

A alta concentração de pessoas em ambas as faixas de rendimento, especialmente aquelas que ganham até 499 reais, aponta para a necessidade urgente de políticas públicas que possam proporcionar suporte imediato. Esses indivíduos são vulneráveis a crises e dependem de ajuda para suprir suas necessidades básicas.

- **Cenário de Recuperação:**

A quantidade significativa de pessoas nas faixas de 0 a 999 reais destaca os desafios da recuperação econômica pós-pandemia. Para que essa recuperação tenha sido eficaz, é fundamental termos estratégias que garantam acesso ao mercado de trabalho e incentivem o aumento de rendimentos.

A situação de 106.419 indivíduos sem rendimento e a quantidade de pessoas com rendimentos até 999 reais é um chamado à ação para governantes e sociedade civil. Medidas urgentes são necessárias para enfrentar crises e garantir que aqueles em condições extremas de vulnerabilidade recebam o suporte necessário para reconstruir suas vidas.
""")

st.header("Conclusão")

st.markdown("""
A análise da crise provocada pela pandemia de covid-19 revela a urgência de medidas eficazes por parte do governo e das instituições para apoiar aqueles que se encontram em situação de vulnerabilidade. Em momentos de crise de saúde pública, como a que vivemos, é crucial que haja um esforço coordenado para auxiliar pessoas que não possuem fontes de renda ou trabalhos que possibilitem a atuação remota. A ausência de apoio econômico pode agravar ainda mais a desigualdade social e aumentar o sofrimento de comunidades já fragilizadas.

As políticas de assistência devem ser rápidas, abrangentes e acessíveis, garantindo que os recursos cheguem de forma eficiente aos mais necessitados. Programas de auxílio emergencial, distribuição de alimentos e acesso a serviços de saúde são fundamentais para mitigar os impactos econômicos e sociais de uma crise.

Além disso, é importante refletir sobre como podemos nos preparar para futuras pandemias. Algumas sugestões incluem:

**1 - Fortalecimento da Rede de Proteção Social:** Investir em programas que garantam uma rede de segurança para os mais vulneráveis, independentemente de crises.

**2 - Desenvolvimento de Plataformas Remotas:** Incentivar a adoção de tecnologias que possibilitem a continuidade do trabalho remoto, garantindo que as pessoas possam manter suas atividades profissionais mesmo em situações adversas.

**3 - Educação e Capacitação:** Promover treinamentos e cursos que ajudem a população a adquirir novas habilidades, facilitando a adaptação a novas realidades de trabalho e economia.

**4 - Colaboração Multissetorial:** Fomentar parcerias entre governo, setor privado e sociedade civil para criar soluções inovadoras que possam ser implementadas rapidamente em resposta a crises futuras.

**5- Planejamento e Simulação:** Desenvolver planos de contingência que incluam simulações de pandemias, ajudando as instituições a se prepararem melhor para cenários futuros.

Através dessas ações, podemos construir uma sociedade mais resiliente e solidária, capaz de enfrentar não apenas crises de saúde, mas também os desafios econômicos e sociais que delas emergem. A experiência adquirida durante a pandemia deve servir como um catalisador para transformações positivas e sustentáveis em nossa sociedade.

""") 
