import requests

# Definindo o token obtido
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI0MCwiaWF0IjoxNzMzMzQ4MDI2LCJleHAiOjE3MzM0MzQ0MjZ9.iJdwzunOY5Oly1WmdzidTkkC7sGKFPrmJ-U-6Gnp7tg'

# URL do endpoint para listar os produtos do usuário
product_url = "http://apipf.jogajuntoinstituto.org/"

# Cabeçalho com o token de autorização
headers = {
    'Authorization': f'Bearer {token}',
    'accept': 'application/json',  # Definindo o tipo de resposta esperada como JSON
}

# Fazendo a requisição GET para buscar a lista de produtos
response = requests.get(product_url, headers=headers)

# Verificando a resposta da requisição
if response.status_code == 200:
    products = response.json()  # Obtendo a lista de produtos como JSON
    if products:  # Verificando se há produtos cadastrados
        print("Lista de Produtos Cadastrados:")
        for product in products:
            print(f"ID: {product['idprodutos']}")
            print(f"Nome: {product['name']}")
            print(f"Descrição: {product['description']}")
            print(f"Preço: {product['price']}")
            print(f"Categoria: {product['category']}")
            print(f"Frete: {product['shipment']}")
            print(f"Imagem: {product['image']}")
            print("-" * 40)  # Separador para visualização
    else:
        print("Nenhum produto cadastrado para este usuário.")
else:
    print(f"Falha ao buscar os produtos. Status code: {response.status_code}")
    print("Detalhes do erro:", response.json())
