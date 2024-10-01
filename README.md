## 📚 The Dog API Performance Testing<br>
Descrição<br>
Este projeto contém scripts de automação de testes de performance para a The Dog API utilizando o Locust, uma ferramenta de testes de carga distribuída e de desempenho em Python. Aqui, testamos endpoints da API como listagem de raças de cães, envio de imagens e outros serviços oferecidos pela The Dog API.

## Funcionalidades <br>
📦 Teste de Performance: Testes de carga distribuída usando Locust.<br>
🌐 Integração com The Dog API: Testes executados diretamente contra os endpoints da API.<br>
📊 Relatórios: Resultados dos testes de carga, como tempo de resposta, taxa de sucesso e falha, entre outros.<br>
🔄 Scripts Automatizados: Testes totalmente automatizados prontos para serem executados em diferentes ambientes.<br>

## Tecnologias Utilizadas <br>
Linguagem: Python 3.x
Ferramentas de Teste: Locust
Requisições HTTP: requests e locust.HttpUser

## Pré-requisitos
Python 3.x instalado.
Locust

## Clone este repositório:

1. Clone o repositório:

    ```bash
   git clone https://github.com/seu-usuario/api-dog-performance-tests.git
   cd api-dog-performance-tests
    ```
    
2. Instale as dependências:
   
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar os Testes
  Testes Locust (Performance)

  Execute o Locust apontando para o arquivo de testes locustfile.py:

   ```bash
   locust -f locustfile.py --host https://api.thedogapi.com
   ```
Acesse http://localhost:8089 no navegador para iniciar o teste de carga e monitorar os resultados em tempo real.

## Parâmetros de Execução
   Número de usuários simultâneos: Defina no painel do Locust.
   Taxa de crescimento de usuários: Configurável no painel ou diretamente no código.

## Testes de API Incluídos
   -> Listagem de Raças com Paginação <br>
   -> Obter Informações de uma Raça Específica <br>
   -> Buscar Imagens Aleatórias de Cães com Parâmetros <br>
   -> Cadastro de Votos em Imagens de Cães <br>
   -> Envio de Imagens <br>
   -> Votações de Raças


Imagens geradas:

Com 1 usuário:
![total_requests_per_second_1727792709 229](https://github.com/user-attachments/assets/ce6f956a-54b1-4ba5-835a-9a320423d9b4)

Com 10 usuários:
![total_requests_per_second_1727792935 08](https://github.com/user-attachments/assets/188b18f3-816d-4988-a5ad-3ed7a4b0970c)
