#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_utils.py
----------------------------------

Tests for `dbfkit.utils` module.
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from dbfkit.utils import UnicodeReader, UnicodeWriter, smart_open
from StringIO import StringIO


def test_unicodereader_next():
    """ Test the UTF-8 reader """
    with open('data/test_utf8.csv') as csvfile:
        reader = UnicodeReader(csvfile, encoding='utf-8')
        assert reader.next() == ['a', 'b', 'c']
        assert reader.next() == ['1', '2', '3']
        assert reader.next() == ['4', '5', 'ʤ']


def test_unicodereader():
    """ Test UnicodeReader as an iterator """
    test_data = [['a', 'b', 'c'],
                 ['1', '2', '3'],
                 ['4', '5', 'ʤ']]
    with open('data/test_utf8.csv') as csvfile:
        reader = UnicodeReader(csvfile, encoding='utf-8')
        for i, row in enumerate(reader):
            assert row == test_data[i]


def test_unicodewriter():
    """ Test the UTF-8 CSV Writer """
    stream = StringIO()
    writer = UnicodeWriter(stream, encoding='utf-8')
    writer.writerows([['a', 'b', 'c']])
    assert stream.getvalue() == "a,b,c\r\n"


def test_smart_open():
    """ Test the smart_open function """
    stream = StringIO()
    with smart_open(stream) as csvfile:
        writer = UnicodeWriter(csvfile)
        writer.writerow(['a', 'b', 'c'])
        assert stream.getvalue() == 'a,b,c\r\n'
