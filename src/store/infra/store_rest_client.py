import requests

from src.store.domain.store import Store


def api_rest_get_method(url):
    response = requests.get(url)
    response_json = response.json()
    return response_json


def store_rest_client() -> list:
    url = 'empty_url'
    response_json = api_rest_get_method(url)

    stores = []
    for response_json_wh in response_json['data']:
        store_id = response_json_wh['storeId']
        store_local_datetime = response_json_wh['storeLocalDateTime']
        store = Store(store_id, store_local_datetime)
        stores.append(store)

    return stores
