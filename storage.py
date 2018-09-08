import sqlite3
from typing import NamedTuple

class QueryTemplate(NamedTuple):
    name: str
    url_template: str
    id: int = None
    icon_url: str = None
    hits: int = 0

class Storage:

    _DB_VERSION = 1
    _DB_FILE_PATH = 'db.sqlite3'

    def __enter__(self):
        self.db = sqlite3.connect(self._DB_FILE_PATH)
        self.db.row_factory = sqlite3.Row
        self.db.executescript('''
            create table if not exists misc (
                key text primary key,
                n integer,
                s text,
                b blob
            );
            create table if not exists query_template (
                id integer primary key,
                name text not null,
                url_template text not null,
                icon_url text
            );
        ''')
        self.db.execute(
            "insert or ignore into misc (key, n) values ('version', ?)",
            [ self._DB_VERSION ])
        self.db.commit()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.db.rollback()
        else:
            self.db.commit()
        self.db.close()

    def pw_is_set(self):
        c = self.db.execute("select 1 from misc where key = 'password'")
        return bool(c.fetchone())

    def pw_get(self):
        c = self.db.execute("select b from misc where key = 'password'")
        return c.fetchone()[0]

    def pw_set(self, password):
        self.db.execute(
            "insert or replace into misc (key, b) values ('password', ?)",
            [ password ])

    def tpl_add(self, tpl):
        self.db.execute('''
            insert into query_template
            (name, url_template, icon_url) values (?,?,?)''',
            [ tpl.name, tpl.url_template, tpl.icon_url ])
        self.db.commit()
        id = self.db.execute('select last_insert_rowid()').fetchone()[0]
        return tpl._replace(id = id)

    def tpl_get_all(self):
        return [
            QueryTemplate(**row)
                for row in self.db.execute('''
                    select id, name, url_template, icon_url
                    from query_template''') ]

    def tpl_set_icon_url(self, tpl, icon_url):
        self.db.execute(
            'update query_template set icon_url = ? where id = ?',
            [ icon_url, tpl.id ])
        self.db.commit()

