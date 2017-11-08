# -*- coding: utf-8 -*-
import pytest
from . import assert_warn
from django_rediser import RedisStorage


class TestParser:
    def test__connect(self):
        rs = RedisStorage()
        rs.connect()
        assert rs._db is not None
