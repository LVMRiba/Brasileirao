# Brasileirao
Análise de Dados com o Campeonato Brasileiro de pontos corridos

### FUTURE PLANS:
- :heavy_check_mark: Modularizar Código
- Otimizar Fonte de Dados
- :heavy_check_mark: Criar Interface Gráfica
- Histórico de Confrontos
- Análise de dados quanto aos pontos corridos (League Trophy)
- Análise de dados quanto aos resultados do 1ºturno (Opening Trophy)
- Análise de dados quanto aos resultados do 2ºturno (Closing Trophy)
- Análise de dados quanto aos resultados como Mandante (Home Trophy)
- Análise de dados quanto aos resultados como Visitante (Away Trophy)
- Análise de dados quanto ao rebaixamento por desempenho recente (Rebaixamento Promédio)
- Análise de dados quanto ao placar agregado (Aggregate Trophy)
- Rendimento por rodadas
- Previsão de Resultados (necessário aprendizado e uso de Machine Learning)

### CHANGELOG:

#### 0.32
- Modularização ampla do código
- Criação do módulo "generators". Módulo de criação de dados
- Criação do módulo "files". Módulo de controle de arquivos
- Criação do módulo "manager". Módulo de transformação de dados
- Criação do módulo "main_library". Módulo de importação das bibliotecas
- Arquivamento de códigos ultrapassados na pasta "old files" 

#### 0.28
- Biblioteca Tkinter: Habilitação de Interface Gráfica
- Criação do módulo "main". O novo módulo principal do projeto.
- Transição do Corpo do Código para uso de Classes
- Transição dos nomes e comentários para o Inglês

#### 0.22
- Criação do módulo "module_gen"
- Criação do módulo "module_alterar"

#### 0.20
- Criação da função "gerar_tabela_agregado"
- Adição de nova tabela "agregate_campaign.csv"
- Leitura da tabela "agregate_campaign.csv"
- Mudança de nome de função: "write_file" -> "write_file_campaign"

#### 0.15
- Criação da função "write_file"
- Adição de nova tabela "table_campaign.csv"
- Leitura da tabela "table_campaign.csv"

#### 0.11
- Adição de nova tabela "pontosasterisco.csv"
- Leitura da tabela "pontosasterisco.csv"

#### 0.1
- Criação da função "alterar_arena"
- Criação da função "alterar_clube"
- Criação da função "gerar_tabela_campanha"
- Criação da função "gerar_tabela_edicao"
- Criação da função "gerar_tabela_resultado"
- Criação da função "gerar_lista_clube_ano"
- Criação da função "print_list"
- Adição de novas tabelas (Partidas e Estatísticas)
- Configuração das opções de visualização de tabela (SET_OPTION)
- Leitura de dados através de Biblioteca de Pandas
- Tratamento da fonte de dados
