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
    # test_get_number = Info(("男", "-", 182, 95)).getNumber()
    test_get_number = Info("男-北京-187-89")
    test_result = test_get_number.getNumber("男-上海-182-95")
    test_result_location = test_get_number.getLocation()
    assert test_result == ['182','95']
    assert test_result_location == ['男', '北京']

    print("ok")

def test_Info_sortWord():
    test_get_number = Info("男-北京-187-89")
    test_result_word = test_get_number.sortWord()
    assert test_result_word == '北京市'