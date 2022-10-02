from src.store.usecase.local_date import local_date
from src.store.domain.store import Store


def test_local_date(mocker):

    mocker.patch(
        'src.store.usecase.local_date.store_rest_client',
        return_value=[
            Store(id='SPAIN', local_datetime='2022-09-24T15:00:00'),
            Store(id='FRANCE', local_datetime='2022-09-24T15:00:00')
            ]
    )

    response = local_date(store_id='SPAIN')
    assert response == '2022-09-24'
    assert type(response) == str

    response = local_date(store_id='FRANCE')
    assert response == '2022-09-24'
    assert type(response) == str

    response = local_date(store_id='NONE')
    assert response == None
