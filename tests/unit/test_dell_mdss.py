import pytest

from pytest_checkmk.check import OK, WARNING
from pytest_checkmk.snmpoutput import SNMPOutput
from io import StringIO

def test_snmp_scan_function(snmp_check):
    oid = SNMPOutput('.1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.674.10893.2.31')

    assert snmp_check.snmp_scan_function(oid) == True

def test_snmp_scan_function(snmp_check):
    oid = SNMPOutput('.1.3.6.1.2.1.1.2.0 = OID: .1.3.6.1.4.1.42')

    assert snmp_check.snmp_scan_function(oid) == False

def test_inventory(snmp_check):
    checks = snmp_check.inventory_function([('NAME',)])
    assert len(checks) == 1
    assert checks[0] == ('NAME', {})

def test_check_ok(snmp_check):
    res = snmp_check.check_function('NAME', {}, [('NAME','WWID', 'Vend', 'Prod', 'Mod', '0')])

    assert res == OK
    assert res != "Needs Attention"

def test_check_needs_attention(snmp_check):
    res = snmp_check.check_function('NAME', {}, [('NAME','WWID', 'Vend', 'Prod', 'Mod', '1')])

    assert res == WARNING
    assert res == "Needs Attention"
