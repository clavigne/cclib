# -*- coding: utf-8 -*-
#
# Copyright (c) 2017, the cclib development team
#
# This file is part of cclib (http://cclib.github.io) and is distributed under
# the terms of the BSD 3-Clause License.

"""Facilities for moving parsed data to other cheminformatic libraries."""

from cclib.parser.utils import find_package

if find_package("Bio"):
    from cclib.bridge.cclib2biopython import makebiopython

if find_package("openbabel"):
    from cclib.bridge.cclib2openbabel import makeopenbabel

if find_package("PyQuante"):
    from cclib.bridge.cclib2pyquante import makepyquante

if find_package("psi4"):
    from cclib.bridge.cclib2psi4 import makepsi4


del find_package
