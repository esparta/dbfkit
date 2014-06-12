# -*- coding: utf-8 -*-

"""
test_dbfkit
----------------------------------

Tests for `dbfkit.cli` module.
"""

from click.testing import CliRunner
from dbfkit.cli import dbfread

CSVRESULT = "data/catalogo.csv"
DBFFILE = 'data/catalogo.dbf'


def test_passing_inputfile():
    """ Test the command line. Output to stdout """
    with open(CSVRESULT, "rb") as csvfile:
        output = csvfile.read()

    runner = CliRunner()
    result = runner.invoke(dbfread, [DBFFILE, '-'])
    assert result.exit_code == 0
    assert result.output.split() == output.split()
