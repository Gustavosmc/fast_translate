<h1>fast_translate</h1>

<p>Traduz com audio um texto em outro idioma para Português, basta selecionar o texto que se quer traduzir em paginas da web ou documentos no desktop e pressionar Control +
Barra de Espaço </p>


<h2> Instalação </h2>

1 - É necessário que você tenha o python3.4 ou maior instalado:

  Linux: O Linux já vem com o python3 instalado
  
  Windows: veja como instalar o Python no Windows aqui: https://python.org.br/instalacao-windows/

1 - Clone o projeto com git ou faça o download para seu desktop:

  git clone https://github.com/Gustavosmc/fast_translate.git

2 - Instale as dependências usando pip:

  pip install -r requirements.txt

3 - É necessário instalar Sox, com suporte a MP3. 

  No Ubuntu ou derivados do Debian: 
  sudo apt-get install sox libsox-fmt-mp3

  Para usuários de Windows baixem o Sox aqui:
  https://sourceforge.net/projects/sox/files/sox/

  Após instalado você precisa copiar a libmad.DLL que se encontra zipado aqui, para o diretório onde foi instalado o Sox,
  e adicionar o caminho da instalação do Sox para as variáveis de ambientes do Windows.
  
  <h2> Execução </h2>
  
    No Linux abra um terminal dentro da pasta do fast_translator e execute com:
    python main.py
    
    No Windows, assim como no Linux você pode executar pelo terminal caso tenha o Python configurado no seu Path.
 
