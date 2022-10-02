from datetime import datetime
from typing import Union

from src.store.infra.store_rest_client import store_rest_client


def local_date(store_id: str) -> Union[str, None]:

    stores = store_rest_client()

    for store in stores:
        if store.id == store_id:
            local_datetime = datetime.strptime(store.local_datetime, '%Y-%m-%dT%H:%M:%S')
            return local_datetime.strftime('%Y-%m-%d')
    return None
