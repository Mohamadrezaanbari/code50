import pytest
from project import check_correct_args, select_Geographical_region, select_height


def test_check_correct_house():
    with pytest.raises(SystemExit):
        check_correct_args()


def test_select_Geographical_region():
    assert select_Geographical_region("Stark") == "North"
    assert select_Geographical_region("Targaryen") == "South"
    assert select_Geographical_region("Lannister") == "South"
    assert select_Geographical_region("Baratheon") == "South"
    assert select_Geographical_region("Greyjoy") == "North"
    assert select_Geographical_region("Mormont") == "North"
    assert select_Geographical_region("no dynasty") == "None"



def test_select_height():
    assert select_height(1.73) == 5.7
    assert select_height(1.57) == 5.1
    assert select_height(1.82) == 6

