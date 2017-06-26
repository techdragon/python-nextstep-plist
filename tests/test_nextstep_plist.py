
import nextstep_plist


def test_loads():
    assert nextstep_plist.loads('{"x" = "1"; "y" = "2";}') == {u'x': u'1', u'y': u'2'}


def test_loads():
    assert nextstep_plist.loads('{"x" = "1"; "y" = "2";}') == {u'x': u'1', u'y': u'2'}
