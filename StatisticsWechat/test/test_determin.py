from StatisticsWechat.determine import Info
import pytest


def test_Info_sortNum():
    test_info = Info([182, 96, 1]).sortNum([90, 183, 23])
    assert type(test_info) == list
    assert len(test_info) == 2
    assert test_info[0] == 183
    assert test_info == [183, 90]
    # print(test_info)


def test_Info_getLocation():
    test_get_number = Info(["男", "-", 182, 95]).getNumber()
    assert test_get_number == [182, 95]
