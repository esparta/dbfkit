# -*- coding: utf-8 -*-

"""
test_dbfkit
----------------------------------

Tests for `dbfkit` module.
"""


from dbfkit import DBFUtils
from dbfkit.utils import smart_open
from StringIO import StringIO

from os import remove


DBF = DBFUtils("data/catalogo.dbf")
CSVRESULT = "data/catalogo.csv"


def test_created():
    """ Test if the Instances was created correctly """
    assert isinstance(DBF, DBFUtils)


def test_returnsrecno():
    """ Test if the number of records exported """
    stream = StringIO()
    recno = DBF.export(stream)
    assert recno == 29


def test_convertedfile():
    """ Test if the file was converted correctly """
    with open(CSVRESULT) as csvfile:
        output = csvfile.read()
    stream = StringIO()
    DBF.export(stream)
    assert stream.getvalue() == output


def test_temporalfile():
    """ Create a file with the results """
    csvfile = "data/test_file.csv"
    with open(CSVRESULT) as rcsvfile:
        output = rcsvfile.read()
    try:
        with smart_open(csvfile) as tmp_file:
            DBF.export(tmp_file)
        with open(csvfile, "r") as tmp_file:
            assert output == tmp_file.read()
    finally:
        remove(csvfile)


def test_nullfields():
    """ Test the export of a DBF with null values """
    odbfnull = DBFUtils("data/withnulls.dbf")
    stream = StringIO()
    odbfnull.export(stream)
    assert stream.getvalue() == open("data/withnulls.csv").read()
