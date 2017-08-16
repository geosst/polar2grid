#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2015 Space Science and Engineering Center (SSEC),
# University of Wisconsin-Madison.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of the polar2grid software package. Polar2grid takes
# satellite observation data, remaps it, and writes it to a file format for
#     input into another program.
# Documentation: http://www.ssec.wisc.edu/software/polar2grid/
#
# Written by David Hoese    January 2015
# University of Wisconsin-Madison
# Space Science and Engineering Center
# 1225 West Dayton Street
# Madison, WI  53706
# david.hoese@ssec.wisc.edu
"""Polar2grid VIIRS Frontend

:author:       David Hoese (davidh)
:author:       Ray Garcia (rayg)
:contact:      david.hoese@ssec.wisc.edu
:organization: Space Science and Engineering Center (SSEC)
:copyright:    Copyright (c) 2015 University of Wisconsin SSEC. All rights reserved.
:date:         Jan 2015
:license:      GNU GPLv3
"""
__docformat__ = "restructuredtext en"

from polar2grid.viirs.swath import Frontend, add_frontend_argument_groups
from polar2grid.viirs.edr_swath import EDRFrontend, add_frontend_argument_groups as add_frontend_argument_groups_edr

# Configure a null handler in case someone is using this as a library (i.e. no warning about not configuring logging)
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

