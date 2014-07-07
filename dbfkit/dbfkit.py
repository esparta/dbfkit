# coding=utf-8
"""
  DBFUtils
  Read a DBF file & convert to csv with UTF-8 encoding

"""
from __future__ import unicode_literals
from __future__ import absolute_import

from dbf import Table
from .utils import UnicodeWriter
from csv import excel
import sys


class DBFUtils(object):
    """ DBF Utils """
    output = sys.stdout

    @staticmethod
    def _opentable(dbfilename=None, codepage=None):
        """ Open the DBF as a Table object """
        return Table(dbfilename, codepage=codepage)

    @classmethod
    def tocsv(cls, dbfilename=None, output=None,
              codepage=None, dialect=excel):
        """ Convert to csv the table to desired output (sys.stdout by default)
        """
        records = 0
        output = output or cls.output
        csvwriter = UnicodeWriter(output, dialect=dialect)
        with cls._opentable(dbfilename=dbfilename,
                            codepage=codepage) as table:
            csvwriter.writerow(table.field_names)
            for records, row in enumerate(table, start=1):
                csvwriter.writerow(['' if field is None
                                    else unicode(field).strip()
                                    for field in row])
            return records
