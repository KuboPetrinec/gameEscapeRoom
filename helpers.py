from typing import List

def get_item_by_name(name: str, items: list) -> dict:
    # check if item is not null
    if not name:
        raise ValueError("Name is empty")

    for item in items:
        if name == item['name']:
            return item

