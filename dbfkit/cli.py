# coding=utf-8
"""
  Usage: python tocsv.py [options] file

  Options:
    -h, --help            show this help message and exit
    -v, --verbose         Verbose logging
    -c CODEPAGE, --codepage=CODEPAGE
                          Use specific codepage, if not supplied, use the
                          table's codepage
  Example:
    python tocsv.py -c cp1252 catalogo.dbf
"""
from __future__ import unicode_literals
from __future__ import absolute_import

from dbfkit import DBFUtils

import click
import sys


@click.command()
@click.argument('inputfile', type=click.File('rb'))
@click.argument('output', type=click.File('wb'),
                required=False, default=sys.stdout)
@click.option('-c', '--codepage', default=None,
              help="Use specific codepage, if not supplied,"
                   " use the table's codepage")
def dbfread(inputfile, output, codepage):
    """ Convert a DBF file to csv on desired output (stdout by default) """

    dbf = DBFUtils(dbffile=inputfile.name, output=output, codepage=codepage)
    dbf.export()


if __name__ == '__main__':
    dbfread()
