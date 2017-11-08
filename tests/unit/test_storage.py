# -*- coding: utf-8 -*-
import pytest
from . import assert_warn
from django_rediser import RedisStorage


class TestParser:
    def test__init(self):
        rs = RedisStorage()
        assert rs.connect()
