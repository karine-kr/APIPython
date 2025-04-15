import requests

class TestPetStoreUserAPI:
    url = "https://petstore.swagger.io/v2"
    headers = {"Content-Type": "application/json"}

    user_data = {
        "id": 0,
        "username": "Tiague",
        "firstName": "testeefvdfe",
        "lastName": "Kfefdsf",
        "email": "teste@teste.com.br",
        "password": "12345",
        "phone": "5135625678",
        "userStatus": 0
    } 

    update_user_data = {
        "id": 0,
        "username": "Happt",
        "firstName": "KarineAtualizado",
        "lastName": "KAtualizado",
        "email": "novoteste@teste.com.br",
        "password": "54321",
        "phone": "09876543",
        "userStatus": 0
    }


    def test_post_object(self):
        post_response = requests.post(f"{self.url}/user", json=self.user_data, headers=self.headers)
        print("status Code:", post_response.status_code)
        print("Response Body:", post_response.json())
        assert post_response.status_code == 200


    def test_get_object(self):
            get_response = requests.get(f"{self.url}/user/{self.user_data['username']}", headers=self.headers)
            print("status Code:", get_response.status_code)
            print("Response Body:", get_response.text)

            assert get_response.status_code == 200
            response_data = get_response.json()

            for key in self.user_data:
                if key != "id" and key in response_data:
                    assert key in response_data, f"Campo '{key}' não encontrado no retorno da API"
                    assert response_data[key] == self.user_data[key], (
                        f"Campo '{key}' diferente: esperado={self.user_data[key]}, recebido={response_data[key]}"
                )
                else:
                    print(f"Ignorando campo '{key}'")

    def test_put_object(self):
        put_response = requests.put(f"{self.url}/user/{self.user_data['username']}", json=self.update_user_data, headers=self.headers)
        print("status Code:", put_response.status_code)
        print("Response Body:", put_response.text)
        assert put_response.status_code == 200

        
        get_response_update = requests.get(f"{self.url}/user/{self.update_user_data['username']}", headers=self.headers)
        print("status Code após PUT:", get_response_update.status_code)
        print("Response Body após PUT:", get_response_update.json())
        assert get_response_update.status_code == 200

        response_data = get_response_update.json()
        for key in self.update_user_data:
            if key != "id" and key in response_data:
                assert response_data[key] == self.update_user_data[key], f"{key} não atualizado corretamente"

    def test_delete_object(self):
        username = self.update_user_data["username"]

        delete_response = requests.delete(f"{self.url}/user/{username}", headers=self.headers)
        print("Delete status Code:", delete_response.status_code)
        print("Delete Response Body:", delete_response.text)
        assert delete_response.status_code == 200

        get_response_delete = requests.get(f"{self.url}/user/{username}", headers=self.headers)
        print("status Code após DELETE:", get_response_delete.status_code)
        print("Response Body após DELETE:", get_response_delete.text)
        assert get_response_delete.status_code == 404