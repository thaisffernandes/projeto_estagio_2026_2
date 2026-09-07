## Projeto “Solicitação e Análise de Pedidos de Paletas Personalizadas”

## Sobre o projeto

Este sistema tem como objetivo viabilizar o envio de pedidos para a fabricação de paletas de corretivo personalizadas. O usuário informa algumas informações pessoais e as características desejadas para a paleta. Após o envio, o pedido é armazenado no banco de dados e fica disponível para análise do administrador interno da empresa, que verifica sua viabilidade de produção.

## Funcionalidades

- Cadastro de solicitações de produtos personalizados;
- Confirmação visual após o envio do pedido;
- Armazenamento dos dados das solicitações em um banco de dados;
- Login do administrador interno por meio de nome de usuário e senha;
- Painel de controle com a visualização dos pedidos recebidos;
- Página para análise individual de cada pedido;
- Envio de uma resposta ao cliente;
- Confirmação ou cancelamento dos pedidos.

## Tecnologias utilizadas
Python: utilizado no desenvolvimento do back-end e na implementação da lógica do sistema. 
 | Flask: utilizado para criar a aplicação web e estabelecer a comunicação entre o código Python e as páginas HTML. 
 | SQLite: utilizado para armazenar os dados das solicitações realizadas pelos usuários. 
 | HTML: utilizado para estruturar o conteúdo das páginas, como títulos, botões, campos de texto e formulários. 
 | CSS: utilizado para a estilização e personalização visual das interfaces.
 | Jinja2: utilizado para conectar dados e informações processadas pelo Python aos elementos das páginas HTML.

## Decisões do Projeto
1. Escolha do tema
O tema foi escolhido após algumas pesquisas no Pinterest e a partir de um vídeo no YouTube. Para encontrar uma referência para o projeto, busquei no Pinterest imagens que remetessem a empresas que trabalham com cadastros e solicitações.
Durante essa pesquisa, encontrei uma imagem relacionada à maquiagem e me lembrei de um vídeo que havia assistido há uns dias atrás sobre como a maquiadora amava construir suas paletas personalizadas. Como era uma informação nova para mim, pesquisei se esse mercado realmente existia e encontrei um site que trabalha dessa maneira. A partir disso, surgiu a ideia de criar um sistema de solicitações no qual determinadas informações precisassem ser analisadas e aprovadas antes da confirmação do pedido.
A ideia me pareceu viável para a vaga porque permite representar um processo de análise de solicitações dentro de uma empresa, além de ser um tema que eu tenho interesse.

2. Escolha da stack
A primeira escolha foi utilizar Python, por ser uma linguagem que considero mais simples, prática e com a qual já tenho familiaridade. Também considerei que ela seria adequada para desenvolver a lógica do sistema.
Para o front-end, escolhi HTML e CSS por serem tecnologias clássicas para essa finalidade e por eu já possuir conhecimentos básicos sobre a função de cada uma delas. Dessa forma, seria mais prático trabalhar com ferramentas que eu já conheço.
Para desenvolver a aplicação web, fiquei inicialmente entre Flask e Django. Optei pelo Flask após pesquisar sobre as duas opções e verificar que ele é adequado para aplicações menores e mais simples, enquanto o Django oferece uma estrutura mais completa, sendo mais adequado para projetos de maior porte.
O Jinja2 foi incluído posteriormente a partir de uma recomendação da IA, principalmente para permitir a utilização de informações processadas pelo Python diretamente nas páginas HTML.

## Estrutura do sistema
O sistema foi estruturado em cinco etapas principais:
1. Solicitação do usuário: preenchimento e envio das informações necessárias para o pedido.
2. Login do administrador: autenticação para acessar a área administrativa.
3. Painel de controle: visualização dos pedidos recebidos.
4. Análise da solicitação: visualização individual das informações de cada pedido e tomada de decisão.
5. Armazenamento dos dados: registro das solicitações e suas respectivas informações no banco de dados.

## Uso de IA

Implementação do Flask:
Antes de utilizar a IA, eu já havia desenvolvido a estrutura inicial em Python e definido como gostaria que cada parte do código funcionasse. A IA foi utilizada como auxílio para implementar o Flask e adaptar essa estrutura para uma aplicação web, permitindo a comunicação entre o código Python e as páginas HTML.

Construção das interfaces HTML/CSS:
As páginas admin.html, analisar.html, index.html e login.html foram construídas com auxílio da Inteligência Artificial. Nos prompts, informei as referências visuais que gostaria que o design seguisse — principalmente a identidade visual da MAC Cosmetics — além dos elementos que deveriam estar presentes em cada interface e, assim, ela criou a estrutura dos códigos HTML e CSS.

Guia do GitHub:
Também utilizei a IA para me guiar em como mexer com a ferramenta fork, pois eu nunca havia utilizado esse modo antes.

## Erros da IA:
Na construção do front-end, eu já tinha em mente que a IA só conseguiria reproduzir o resultado desejado caso as características da interface fossem especificadas de forma clara. Por isso, forneci uma referência visual e descrevi a estética que gostaria de utilizar. Ainda assim, nas primeiras versões foi necessário realizar algumas alterações nas cores e na fonte, pois a interface inicial não correspondia exatamente ao resultado que eu tinha imaginado. Esses ajustes foram ficando menores ao longo do desenvolvimento, porque eu já possuía uma definição mais clara da estética que queria seguir.

Outro erro ocorreu durante a criação da rota @app.route("/login"). A IA adicionou uma parte do código pensando em um sistema de login para o usuário final. Essa funcionalidade não havia sido especificada por mim e não era necessária para o projeto, mas provavelmente foi incluída pela IA como uma tentativa de tornar o sistema mais completo. Como o login deveria ser utilizado apenas pelo administrador interno, fiz a correção manualmente, já que não havia a necessidade de ter essa ferramenta.

Um outro momento foi na parte de definir o tamanho da paleta. A IA sugeriu que o tamanho mínimo fosse 4 e o máximo 10. No entanto, eu queria que o mínimo fosse 2 e o máximo 12. Isso não foi necessariamente um erro, mas algo sutil que poderia passar despercebido e que faria uma diferença no resultado final. Após perceber esse detalhe, fiz a correção de forma manual.
