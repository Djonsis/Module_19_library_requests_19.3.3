import requests

base_url = "https://petstore.swagger.io/v2"

headers = {
    "accept": "application/json"
}

data = {
    "petId": 6,
    "additionalMetadata": "Some metadata"
}


# GET запрос
def get_request():
    url = f"{base_url}/pet/findByStatus"
    response = requests.get(url, headers=headers)
    return response

# POST запрос
def post_request(data):
    url = f"{base_url}/pet"
    response = requests.post(url, json=data, headers=headers)
    return response

# PUT запрос
def put_request(pet_id, data):
    url = f"{base_url}/pet"
    response = requests.put(url, json=data, headers=headers)
    return response

# DELETE запрос
def delete_request(pet_id):
    url = f"{base_url}/pet/{pet_id}"
    response = requests.delete(url, headers=headers)
    return response

# Выполнение запросов и печать ответов
if __name__ == "__main__":
    # Выполнение GET запроса
    get_response = get_request()
    print("GET Response:")
    print(get_response.status_code)
    print(get_response.json())
    print()

    # Выполнение POST запроса
    new_pet_data = {
        "name": "Fluffy",
        "type": "Cat"
    }
    post_response = post_request(new_pet_data)
    print("POST Response:")
    print(post_response.status_code)
    print(post_response.json())
    print()

    # Получение ID нового питомца из POST-ответа
    new_pet_id = post_response.json()["id"]

    # Выполнение PUT запроса
    updated_pet_data = {
        "name": "Whiskers",
        "type": "Cat"
    }
    put_response = put_request(new_pet_id, updated_pet_data)
    print("PUT Response:")
    print(put_response.status_code)
    print(put_response.json())
    print()

    # Выполнение DELETE запроса
    delete_response = delete_request(new_pet_id)
    print("DELETE Response:")
    print(delete_response.status_code)
    print(delete_response.text)
