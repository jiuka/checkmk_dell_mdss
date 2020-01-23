import pytest


def test_no_check(snmp_check):
    results = snmp_check.results('')

    assert results == []

def test_check(snmp_check):
    results = snmp_check.results('''
        .1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.674.10893.2.31
        .1.3.6.1.4.1.674.10893.2.31.500.1.1.0 = STRING: NAME
        .1.3.6.1.4.1.674.10893.2.31.500.1.2.0 = STRING: 0123456789abcdef0123456789abcdef
        .1.3.6.1.4.1.674.10893.2.31.500.1.4.0 = STRING: DELL
        .1.3.6.1.4.1.674.10893.2.31.500.1.5.0 = STRING: MD34xx
        .1.3.6.1.4.1.674.10893.2.31.500.1.6.0 = STRING: 2701
        .1.3.6.1.4.1.674.10893.2.31.500.1.7.0 = INTEGER: 0''')

    assert results == [
        'OK: DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef)'
    ]


def test_check_warn(snmp_check):
    results = snmp_check.results('''
        .1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.674.10893.2.31
        .1.3.6.1.4.1.674.10893.2.31.500.1.1.0 = STRING: NAME
        .1.3.6.1.4.1.674.10893.2.31.500.1.2.0 = STRING: 0123456789abcdef0123456789abcdef
        .1.3.6.1.4.1.674.10893.2.31.500.1.4.0 = STRING: DELL
        .1.3.6.1.4.1.674.10893.2.31.500.1.5.0 = STRING: MD34xx
        .1.3.6.1.4.1.674.10893.2.31.500.1.6.0 = STRING: 2701
        .1.3.6.1.4.1.674.10893.2.31.500.1.7.0 = INTEGER: 1''')

    assert results == [
        'WARNING: DELL MD34xx 2701 (WWID: 0123456789abcdef0123456789abcdef), Needs Attention'
    ]
