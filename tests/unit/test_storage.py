# -*- coding: utf-8 -*-
from django_rediser import RedisStorage


class TestStorage:
    def test_connect(self):
        rs = RedisStorage()
        rs.connect()
        assert rs._db is not None
