# coding=utf-8
"""
Usage: dbf2csv [OPTIONS] INPUTFILE [OUTPUT]

  Convert a DBF file to csv on desired output (stdout by default)

Options:
  -c, --codepage TEXT  Use specific codepage, if not supplied, use the table's
                       codepage
  --version            Show the version and exit.
  --help               Show this message and exit.

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
@click.version_option()
def dbfread(inputfile, output, codepage):
    """ Convert a DBF file to csv on desired output (stdout by default) """

    dbf = DBFUtils(dbffile=inputfile.name, output=output, codepage=codepage)
    dbf.export()


if __name__ == '__main__':
    dbfread()
