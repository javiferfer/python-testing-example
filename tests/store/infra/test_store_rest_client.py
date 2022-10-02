from src.store.infra.store_rest_client import store_rest_client
from src.store.domain.store import Store


def test_store_rest_client(mocker):

    mocker.patch(
        'src.store.infra.store_rest_client.api_rest_get_method',
        return_value={
            "data": [
            {
            "storeId": "SPAIN",
            "storeLocalDateTime": "2022-09-27T15:12:45"
            },
            {
            "storeId": "FRANCE",
            "storeLocalDateTime": "2022-09-27T08:12:45"
            }
            ]
        }
    )

    stores = store_rest_client()
    
    assert stores[0].id == 'SPAIN'
    assert stores[1].id == 'FRANCE'
