# -*- coding: utf-8 -*-
import pytest
from . import assert_warn
from django_rediser import RedisStorage


class TestParser:
    @pytest.fixture(scope='class', autouse=True)
    def init(self):
        self.rs = RedisStorage()

    def test__init(self):
        assert self.rs.connect()
