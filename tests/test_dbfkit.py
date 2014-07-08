# -*- coding: utf-8 -*-

"""
test_dbfkit
----------------------------------

Tests for `dbfkit` module.
"""

from dbfkit import DBFUtils
from dbfkit.utils import smart_open
from StringIO import StringIO
import pytest
from os import remove


@pytest.fixture(scope="function", params=[
    {'name': 'data/catalogo', 'records': 29},
    {'name': 'data/withnulls', 'records': 2}])
def dbfs(request):
    """ Fixture to test all the DBF files against """
    return request.param


def test_convertedfile(dbfs):
    """ Test if the DBF was converted correctly """
    stream = StringIO()
    records = DBFUtils.tocsv(dbfilename=dbfs['name']+".dbf", output=stream)
    assert stream.getvalue() == open(dbfs['name']+".csv").read()
    assert records == dbfs['records']


def test_temporalfile(dbfs):
    """ Create a file with the results """
    csvfile = "data/test_file.csv"
    output = open(dbfs['name']+".csv").read()
    try:
        with smart_open(csvfile) as tmp_file:
            records = DBFUtils.tocsv(dbfilename=dbfs['name']+".dbf",
                                     output=tmp_file)
        assert output == open(csvfile, "r").read()
        assert records == dbfs['records']
    finally:
        remove(csvfile)
