from src.store.domain.store import Store


def test_store(mocker):
    store = Store(
        id='SPAIN',
        local_datetime='2022-06-04T16:05:47'
    )

    assert store.id == 'SPAIN'
    assert store.local_datetime == '2022-06-04T16:05:47'
