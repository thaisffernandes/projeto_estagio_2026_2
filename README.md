## Sobre o projeto
O projeto é baseado na fabricação de paletas de corretivo personalizadas. O cliente faz a solicitação com base nas suas necessidades, e o administrador interno deve acompanhar e analisar a viabilidade da produção.

## Estrutura do sistema
A aplicação apresenta o sistema utilizado para a criação de quatro páginas.

A primeira é direcionada ao usuário final, na qual é permitido realizar a solicitação de um pedido a partir de algumas informações: nome, e-mail, cores, tamanho da paleta, quantidade desejada e um prazo. Todos esses elementos são enviados para o banco de dados.

A segunda página trata-se de onde o administrador irá realizar o login. Há um nome de usuário pré-definido no código, juntamente com a senha, e apenas com esses dois dados é possível que o login seja efetivado. Caso contrário, aparecerá uma mensagem informando “Usuário ou senha incorretos”.

Nome de usuário: nome_adm | Senha: 123 (linha 78 do arquivo app.py)

Já a terceira página é acessada após a realização do login. Neste local, estarão reunidos todos os pedidos que serão guardados no banco de dados. Os pedidos são mostrados de acordo com a ordem em que foram criados, indo do mais recente para o mais antigo. Essa página possui total relação com a primeira, pois só aparecerão os pedidos que forem enviados através dela. Caso não tenha nenhum, aparecerá que há 0 pedidos.

Como uma continuação da funcionalidade anterior, caso o administrador clique em “Analisar situação”, ele será enviado para a análise da solicitação. Nessa aba, será possível ver o pedido de forma individual, escrever uma mensagem para o cliente e confirmar ou cancelar o pedido.

## De forma resumida, temos:
Solicitação do pedido
Login do administrador
Painel com todos os pedidos
Análise individual de cada solicitação

## Pré-requisitos
Visual Studio Code |
Python 3.14.3 |
Flask 3.1.3 

## Passo a passo
1º passo: Instalação
Instale no seu VS Code as seguintes ferramentas: Python e a biblioteca Flask.

2º passo: Criação da pasta
Você deverá criar uma pasta específica para esse programa. O nome fica a seu critério.

3º passo: Criação do arquivo app.py
Dentro da pasta criada anteriormente, deve ser criado um arquivo denominado app.py, que guardará o código principal em Flask.
O código que deverá ser inserido está no arquivo com o mesmo nome no repositório (app.py). Insira-o no seu VS Code.

4º passo: Criação da pasta templates
Após isso, será necessário criar outro arquivo dentro da pasta criada no 2º passo. Essa pasta deve se chamar templates.

Dentro do arquivo templates, devem ser criados outros 4 arquivos e colocado cada um dos códigos correspondentes, que estão disponíveis neste repositório.
Lembre-se de salvar cada arquivo com Ctrl + S.

Arquivo 1: admin.html
Arquivo 2: analisar.html
Arquivo 3: index.html
Arquivo 4: login.html
Obs.: A ordem não fará diferença, mas é fundamental a criação dos 4 arquivos.

5º passo: Execução do programa
Nessa etapa, você já deve ter cada um dos códigos no seu VS Code. O próximo passo será rodar o código do arquivo app.py.
Ao fazer isso, você receberá uma linha no seu terminal escrito:
Running on http://127.0.0.1:5000
Copie esse endereço.

6º passo: Acesso ao sistema
Cole o link anterior no seu navegador. Ao fazer isso, você será direcionado para a página em que são feitas as solicitações do produto.

Para acessar a página de login do administrador, basta acrescentar /login ao final do link.
Após realizar o login corretamente (o nome de usuário e a senha estão explícitos na “Estrutura do Sistema”), o administrador será direcionado para o painel, onde poderá visualizar os pedidos realizados e acessar a opção “Analisar situação” de cada solicitação.
Obs.: Não feche o VS Code durante essa etapa.

## Importante:
O banco de dados será criado automaticamente ao executar o arquivo app.py.
