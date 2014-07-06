===============================
dbfkit
===============================

.. image:: https://travis-ci.org/esparta/dbfkit.png?branch=master
        :target: https://travis-ci.org/esparta/dbfkit

.. image:: https://coveralls.io/repos/esparta/dbfkit/badge.png
        :target: https://coveralls.io/r/esparta/dbfkit

DBF classes and utilities. For humans

* Free software: Apache license
* Documentation: http://dbfkit.readthedocs.org.

Features
--------


* Console Scripts:
    * dbf2csv: Export a DBF file to csv (utf-8 encoding)
* Classes:
    * DBFUtils: Read a DBF and exposes as a csv file

How to use it
----------

As a Console script:

.. code-block:: bash

    $ dbf2csv --help
    Usage: dbf2csv [OPTIONS] INPUTFILE [OUTPUT]

      Convert a DBF file to csv on desired output (stdout by default)

    Options:
      -c, --codepage TEXT  Use specific codepage, if not supplied, use the table's
                           codepage
      --version            Show the version and exit.
      --help               Show this message and exit.

As a module:

.. code-block:: python

    from dbfkit import DBFUtils
    from cStringIO import StringIO

    stream = StringIO()
    with open("data/catalogo.dbf") as catalogo:
        odbf = DBFUtils(catalogo.name, stream)
        odbf.export()
        output = stream.getvalue()
        print(output)


Credits
----------

* Ethan Furman, author of `dbf` module for python: http://pythonhosted.org/dbf/
* Armin Ronacher, author of `click` an excellent python package to create full beautiful command line interfaces: http://click.pocoo.org/
