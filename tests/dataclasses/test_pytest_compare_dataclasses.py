from dataclasses import dataclass
from dataclasses import field


@dataclass
class SimpleDataObject:
    field_a: int = field()
    field_b: str = field()


def test_dataclasses() -> None:
    left = SimpleDataObject(1, "b")
    right = SimpleDataObject(1, "b")
    assert left == right

    left = SimpleDataObject(1, "b")
    right = SimpleDataObject(1, "c")
    assert left != right
