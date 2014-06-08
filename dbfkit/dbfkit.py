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
import os


CRLF = os.linesep


class DBFUtils(object):
    """ DBF Utils """
    def __init__(self, dbffile, output=None, codepage=None):
        """ Initializer for DBFUtils """
        self.table = None
        self.dbffile = dbffile
        self.output = output or sys.stdout
        self.codepage = codepage

    def _opentable(self, codepage=None):
        """ Try to open the dbf """
        codepage = codepage or self.codepage
        self.table = Table(self.dbffile, codepage=self.codepage)
        return self.table.open() is not None

    def tocsv(self, output=None, dialect=excel):
        """ Write the table to the file object (even sys.stdout) """
        records = 0
        output = output or self.output
        csvwriter = UnicodeWriter(output, dialect=dialect)

        csvwriter.writerow(self.table.field_names)
        for records, row in enumerate(self.table, start=1):
            csvwriter.writerow([unicode(field).strip() for field in row])

        return records

    def export(self, output=None, codepage=None):
        """ Export a DBF file to the desired format """
        self.output = output or self.output
        if self._opentable(codepage=codepage):
            return self.tocsv(output=output)
