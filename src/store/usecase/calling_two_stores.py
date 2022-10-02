from src.store.infra.store_rest_client import store_rest_client


def calling_twice():

    stores_first = store_rest_client()
    stores_second = store_rest_client()

    return stores_first, stores_second
