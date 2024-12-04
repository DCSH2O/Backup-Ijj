import requests

# Definindo o token de autenticação
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI0MCwiaWF0IjoxNzMzMzQ4MDI2LCJleHAiOjE3MzM0MzQ0MjZ9.iJdwzunOY5Oly1WmdzidTkkC7sGKFPrmJ-U-6Gnp7tg'

# URL base da API
base_url = "http://apipf.jogajuntoinstituto.org/"

# Cabeçalho de autenticação
headers = {
    'Authorization': f'Bearer {token}',
    'accept': 'application/json'
}

# Função para listar os produtos cadastrados
def list_products():
    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        products = response.json()
        if products:
            print("Lista de Produtos Cadastrados:")
            for product in products:
                print(f"ID: {product['idprodutos']}")
                print(f"Nome: {product['name']}")
                print(f"Descrição: {product['description']}")
                print(f"Preço: {product['price']}")
                print(f"Categoria: {product['category']}")
                print(f"Frete: {product['shipment']}")
                print(f"Imagem: {product['image']}")
                print("-" * 40)
        else:
            print("Nenhum produto cadastrado.")
    else:
        print(f"Falha ao listar produtos. Status code: {response.status_code}")
        print("Detalhes do erro:", response.json())

# Função para deletar um produto pelo ID
def delete_product(product_id):
    delete_url = f"{base_url}{product_id}"
    response = requests.delete(delete_url, headers=headers)

    if response.status_code == 200:
        print(f"Produto com ID {product_id} deletado com sucesso!")
    else:
        print(f"Falha ao deletar o produto. Status code: {response.status_code}")
        print("Detalhes do erro:", response.json())

# Função principal para interagir com o usuário
def main():
    while True:
        # Listar produtos antes de perguntar pela exclusão
        list_products()

        # Perguntar se o usuário deseja deletar algum produto
        try:
            product_id = int(input("Digite o ID do produto que deseja excluir (ou 0 para sair): "))
            if product_id == 0:
                print("Saindo do programa.")
                break  # Sai do loop e termina o programa

            # Deletar o produto escolhido
            delete_product(product_id)

        except ValueError:
            print("Por favor, insira um número válido para o ID do produto.")

# Executar o código principal
if __name__ == "__main__":
    main()
