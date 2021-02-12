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

import pytest  # type: ignore[import]
from cmk.base.plugins.agent_based.agent_based_api.v1 import (
    Result,
    Service,
    State,
)
from cmk.base.plugins.agent_based import dell_mdss


@pytest.mark.parametrize('section, result', [
    (
        [['NAME', '0123456789abcdef0123456789abcdef', 'DELL', 'MD34xx', '2701', '1']],
        [Service(item='NAME')]
    )
])
def test_discovery_dell_mdss(section, result):
    assert list(dell_mdss.discovery_dell_mdss(section)) == result


@pytest.mark.parametrize('item, section, result', [
    ('', [], []),
    (
        'NAME',
        [['NAME', '0123456789abcdef0123456789abcdef', 'DELL', 'MD34xx', '2701', '0']],
        [
            Result(state=State.OK, summary='DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef)'),
        ]
    ),
    (
        'NAME',
        [['NAME', '0123456789abcdef0123456789abcdef', 'DELL', 'MD34xx', '2701', '1']],
        [
            Result(state=State.OK, summary='DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef)'),
            Result(state=State.WARN, summary='Needs Attention')
        ]
    ),
])
def test_check_dell_mdss(item, section, result):
    assert list(dell_mdss.check_dell_mdss(item, section)) == result
