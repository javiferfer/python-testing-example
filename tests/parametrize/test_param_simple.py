import pytest


@pytest.mark.parametrize("num, output", [(1, 11),(2, 22),(3, 33),(4, 44)])
def test_multiplication_11(num, output):
   assert 11*num == output


@pytest.mark.parametrize(
    "room, neighborhood, expected_room, expected_neighborhood",
    [
        ("Shared room", "Queens", 1, 1),
        ("Private room", "Bronx", 2, 2)
    ],
)
def test_preprocess_mapping_columns(room, neighborhood, expected_room, expected_neighborhood):
   # GIVEN  dataframe with columns to map

   if room == "Shared room":
      room = 1
   else:
      room = 2

   if neighborhood == "Queens":
      neighborhood = 1
   else:
      neighborhood = 2

   # THEN the results must be like expected   
   assert neighborhood == expected_neighborhood
   assert room == expected_room