import pytest
import sqlite3

from fluxt.storage import LocalDatabase

DB_PATH = 'streaming_test.db'


@pytest.fixture
def local():
    return LocalDatabase(DB_PATH, 'my_stream_function')


def test_set_key(local):
    local.set_key('key', 1)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    res = cur.execute('select * from keystore')
    rows = res.fetchall()

    cur.close()
    con.close()

    assert len(rows) == 1


def test_get_key(local):
    val = local.get_key('key')

    assert val == 1

    with pytest.raises(KeyError):
        local.get_key('test')


def test_reset(local):
    local.set_key('key', 1)

    local.reset()

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    res = cur.execute('select * from keystore')
    rows = res.fetchall()

    cur.close()
    con.close()

    assert len(rows) == 0
