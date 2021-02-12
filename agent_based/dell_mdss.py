#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Copyright (C) 2020  Marius Rieder <marius.rieder@durchmesser.ch>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# Example excerpt from SNMP data:
# .1.3.6.1.4.1.674.10893.2.31.500.1.1.0 = STRING: NAME
# .1.3.6.1.4.1.674.10893.2.31.500.1.2.0 = STRING: 0123456789abcdef0123456789abcdef
# .1.3.6.1.4.1.674.10893.2.31.500.1.4.0 = STRING: DELL
# .1.3.6.1.4.1.674.10893.2.31.500.1.5.0 = STRING: MD34xx
# .1.3.6.1.4.1.674.10893.2.31.500.1.6.0 = STRING: 2701
# .1.3.6.1.4.1.674.10893.2.31.500.1.7.0 = INTEGER: 1

from .agent_based_api.v1 import (
    equals,
    register,
    Result,
    Service,
    SNMPTree,
    State,
)

register.snmp_section(
    name = 'dell_mdss',
    detect = equals('.1.3.6.1.2.1.1.2.0', '.1.3.6.1.4.1.674.10893.2.31'),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.674.10893.2.31.500.1',
        oids = [
            '1',  # DELL-MD-SS-06-MIB::ssStorageArrayName.0
            '2',  # DELL-MD-SS-06-MIB::ssStorageArrayWWID.0
            '4',  # DELL-MD-SS-06-MIB::ssVendorID.0
            '5',  # DELL-MD-SS-06-MIB::ssProductID.0
            '6',  # DELL-MD-SS-06-MIB::ssModelName.0
            '7',  # DELL-MD-SS-06-MIB::ssStorageArrayNeedsAttention.0
        ],
    ),
)


def discovery_dell_mdss(section):
    for mdss in section:
        yield Service(item=mdss[0])


def check_dell_mdss(item, section):
    for mdss in section:
        name, wwid, vendor, product, model, attention = mdss

        if not name == item:
            continue

        yield Result(state=State.OK, summary=f'{vendor} {product} {model} (WWID: {wwid})')

        if not int(attention) == 0:
            yield Result(state=State.WARN, summary='Needs Attention')


register.check_plugin(
    name = 'dell_mdss',
    service_name = 'MD %s',
    discovery_function = discovery_dell_mdss,
    check_function = check_dell_mdss,
)
