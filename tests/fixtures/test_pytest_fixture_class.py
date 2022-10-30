import pytest


class TimeLine:
    def __init__(self, instances):
        self.instances = instances


@pytest.fixture(params=[
    [1, 2, 3], [2, 4, 5], [6, 8, 10]
])
def timeline(request):
    return TimeLine(request.param)


def test_timeline(timeline):
    for instance in timeline.instances:
        assert instance % 1 == 0
