Feature: Login e Cadastro de Produto

  Scenario: Login bem-sucedido e cadastro de produto
    Given que eu esteja na página de login
    When eu fizer login com meu email e senha
    And eu adicionar um produto com nome, descrição, preço e imagem
    Then o produto deve ser adicionado com sucesso
