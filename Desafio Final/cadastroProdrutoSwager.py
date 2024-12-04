import requests

# Definindo o token obtido
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI0MCwiaWF0IjoxNzMzMzQ4MDI2LCJleHAiOjE3MzM0MzQ0MjZ9.iJdwzunOY5Oly1WmdzidTkkC7sGKFPrmJ-U-6Gnp7tg'

# URL do endpoint de cadastro de produtos
product_url = "http://apipf.jogajuntoinstituto.org/"

# Dados do produto para cadastro
product_data = {
    'name': 'Produto Diony 04.12.2024 h19:03',           # Nome do produto
    'description': 'teste',    # Descrição do produto
    'price': '13',             # Preço do produto
    'category': 'roupa',       # Categoria do produto
    'shipment': 'gratis'       # Preço do frete
}

# URL da imagem da web
image_url = 'https://iconape.com/wp-content/files/ym/360541/png/360541.png'  # Exemplo de URL de imagem

# Baixando a imagem da URL
image_response = requests.get(image_url)

# Verificando se a imagem foi baixada com sucesso
if image_response.status_code == 200:
    # Cabeçalho de autorização com o token
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json',
    }

    # Fazendo a requisição POST com dados do produto e a imagem
    files = {
        'image': ('360541.png', image_response.content, 'image/png')  # Enviando a imagem
    }
    
    # Enviando os dados junto com a imagem
    response = requests.post(product_url, headers=headers, data=product_data, files=files)

    # Verificando a resposta
    if response.status_code == 200:
        print("Produto cadastrado com sucesso!")
        print("Resposta:", response.json())
    else:
        print(f"Falha ao cadastrar o produto. Status code: {response.status_code}")
        print("Detalhes do erro:", response.json())
else:
    print(f"Erro ao baixar a imagem. Status code: {image_response.status_code}")
