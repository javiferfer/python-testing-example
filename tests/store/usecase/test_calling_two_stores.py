from src.store.usecase.calling_two_stores import calling_twice
from src.store.domain.store import Store


def test_calling_two_stores(mocker):

    mocker.patch(
        'src.store.usecase.calling_two_stores.store_rest_client',
        return_value=Store(id='SPAIN', local_datetime='2022-09-24T15:00:00')
    )

    stores_first, stores_second = calling_twice()

    assert stores_first.id == 'SPAIN'
    assert stores_second.id == 'SPAIN'


def test_calling_two_stores_different(mocker):

    mocker.patch(
        'src.store.usecase.calling_two_stores.store_rest_client',
        side_effect=[3, 5]
    )
    stores_first, stores_second = calling_twice()

    assert stores_first == 3
    assert stores_second == 5


def test_calling_two_stores_different(mocker):

    mocker.patch(
        'src.store.usecase.calling_two_stores.store_rest_client',
        side_effect=[
            [Store(id='SPAIN', local_datetime='2022-09-24T15:00:00'), Store(id='PORTUGAL', local_datetime='2022-09-24T15:00:00')],
            [Store(id='FRANCE', local_datetime='2022-09-24T15:00:00'), Store(id='ITALY', local_datetime='2022-09-24T15:00:00')]
            ]
    )
    stores_first, stores_second = calling_twice()

    assert stores_first[0].id == 'SPAIN'
    assert stores_first[1].id == 'PORTUGAL'
    assert stores_second[0].id == 'FRANCE'
    assert stores_second[1].id == 'ITALY'
