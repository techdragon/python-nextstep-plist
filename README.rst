========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-nextstep-plist/badge/?style=flat
    :target: https://readthedocs.org/projects/python-nextstep-plist
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/python-nextstep-plist.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/python-nextstep-plist

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/python-nextstep-plist?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/python-nextstep-plist

.. |requires| image:: https://requires.io/github/techdragon/python-nextstep-plist/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/python-nextstep-plist/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/techdragon/python-nextstep-plist/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/python-nextstep-plist

.. |version| image:: https://img.shields.io/pypi/v/nextstep-plist.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nextstep-plist

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/python-nextstep-plist/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/python-nextstep-plist/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/nextstep-plist.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nextstep-plist

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nextstep-plist.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nextstep-plist

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nextstep-plist.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nextstep-plist


.. end-badges

nextstep-plist is a python 3 compatible fork of the nsplist package
that provides a parser for the NeXTSTEP plist text-based format.
A common usage is parsing iTunes In App Purchase receipts to be
able to reject them early, without having to make a
request to the iTunes API.

This is distinct from the Apple plist format, which has more
supported types and serialises to XML or binary.

* Free software: MIT license

Installation
============

::

    pip install nextstep-plist

Documentation
=============

https://python-nextstep-plist.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
