from locust import HttpUser, task, between

class DogApiUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://api.thedogapi.com"  # Host da API


    # 1. Listar Raças de Cachorros com Paginação
    @task
    def list_breeds_paginated(self):
        params = {
            'limit': 10,
            'page': 1
        }
        response = self.client.get("/v1/breeds", params=params)
        if response.status_code == 200:
            print("Success: Listed breeds with pagination")
        else:
            print(f"Failed: {response.status_code}")

    # 2. Obter Informações de uma Raça Específica
    @task
    def get_breed_by_id(self):
        breed_id = "1"
        response = self.client.get(f"/v1/breeds/{breed_id}")
        if response.status_code == 200:
            print("Success: Fetched breed by ID")
        else:
            print(f"Failed: {response.status_code}")

    # 3. Buscar Imagens Aleatórias de Cães com Parâmetros
    @task
    def get_random_images(self):
        params = {
            'limit': 5,
            'mime_types': 'jpg,png'
        }
        response = self.client.get("/v1/images/search", params=params)
        if response.status_code == 200:
            print("Success: Fetched random dog images")
        else:
            print(f"Failed: {response.status_code}")

    # 4. Cadastro de Votos em Imagens de Cães
    @task
    def vote_on_image(self):
        headers = {
            "Content-Type": "application/json",
            "x-api-key": "YOUR_API_KEY_HERE"
        }
        body = {
            "image_id": "abc123",
            "sub_id": "user123",
            "value": 1
        }
        response = self.client.post("/v1/votes", json=body, headers=headers)
        if response.status_code == 201:
            print("Success: Voted on image")
        else:
            print(f"Failed: {response.status_code}")

    # 5. Deletar um Voto Existente
    @task
    def delete_vote(self):
        vote_id = "12345"
        headers = {
            "x-api-key": "YOUR_API_KEY_HERE"
        }
        response = self.client.delete(f"/v1/votes/{vote_id}", headers=headers)
        if response.status_code == 200:
            print("Success: Deleted vote")
        else:
            print(f"Failed: {response.status_code}")

    # 6. Buscar Imagens Filtradas por Raça
    @task
    def get_images_by_breed(self):
        params = {
            "breed_id": "1",
            "limit": 3
        }
        response = self.client.get("/v1/images/search", params=params)
        if response.status_code == 200:
            print("Success: Fetched images by breed")
        else:
            print(f"Failed: {response.status_code}")

    # 7. Testar Cenários de Erro
    @task
    def invalid_vote(self):
        headers = {
            "Content-Type": "application/json",
            "x-api-key": "YOUR_API_KEY_HERE"
        }
        body = {
            "image_id": "invalid_id",
            "sub_id": "user123",
            "value": 3
        }
        response = self.client.post("/v1/votes", json=body, headers=headers)
        if response.status_code != 201:
            print(f"Error: {response.status_code} - Invalid vote request")
        else:
            print("Unexpected success: Invalid vote passed")
