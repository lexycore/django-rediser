# -*- coding: utf-8 -*-
from django_rediser import RedisJSON


class TestJSON:
    def test_connect(self):
        rs = RedisJSON()
        rs.connect()
        assert getattr(rs.storage, '_db', None) is not None

    def test_set_get(self):
        rs = RedisJSON()
        rs.set('test_set_get',
               {'number': 123, 'string': 'abc', 'boolean': True})
        data = rs.get('test_set_get')
        assert data['number'] == 123
        assert data['string'] == 'abc'
        assert data['boolean'] is True
