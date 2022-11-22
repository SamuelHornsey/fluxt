import sqlite3
import logging

from fluxt.storage.base import Base

logger = logging.getLogger(__name__)


class LocalDatabase(Base):
    def __init__(self, path, namespace):
        """ init memory storage """
        self.con = sqlite3.connect(path, isolation_level=None)
        self.namespace = namespace

        cur = self.con.cursor()

        try:
            cur.execute('create table keystore(namespace, key, value)')
        except sqlite3.OperationalError:
            logger.warning('keystore table already exists')

        cur.close()

    def reset(self):
        """ reset memory """
        cur = self.con.cursor()

        cur.execute('delete from keystore '
                    'where namespace = ?',
                    (self.namespace, ))

        cur.close()

    def set_key(self, key, value):
        """ set key value """
        cur = self.con.cursor()

        try:
            self.get_key(key)
        except KeyError:
            cur.execute('insert into keystore (namespace, key, value) '
                        'values (?, ?, ?)', (self.namespace, key, value))

            cur.close()
            return

        cur.execute('update keystore '
                    'set value = ? '
                    'where namespace = ? and key = ?',
                    (value, self.namespace, key))
        cur.close()

    def get_key(self, key):
        """ get key value """
        cur = self.con.cursor()

        res = cur.execute('select namespace, key, value '
                          'from keystore '
                          'where key = ?', (key,))

        row = res.fetchone()

        cur.close()

        if not row:
            raise KeyError

        return row[2]
