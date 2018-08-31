"""
Domain Unittest
"""

import unittest

from domain import Domain


class TestDomain(unittest.TestCase):
    """
    Unit test for domains
    """

    def test_contructor_id(self):
        """
        Test if contructed Domain has id attr
        """
        domain = Domain(1, 'test')
        self.assertEqual(domain.id, 1)

    def test_contructor_name(self):
        """
        Test if contructed Domain has name attr
        """
        domain = Domain(1, 'test')
        self.assertEqual(domain.name, 'test')

    def test_contructor_mac(self):
        """
        Test if contructed Domain has mac_addresses attr
        """
        domain = Domain(1, 'test')
        self.assertEqual(domain.mac_addresses, [])

    def test_contructor_num_mac(self):
        """
        Test if contructed with the right number of mac addresses
        """
        for num_mac_addresses in range(3):
            domain = Domain(1, 'test', num_mac_addresses)
            self.assertEqual(len(domain.mac_addresses), num_mac_addresses)

    def test_domain_mac_refer_to_id(self):
        """
        Test if the domain mac_addresses is generated from id
        """
        mapping_id_mac_address = [
            (1, '00:01'),
            (10, '00:0A'),
            (16**4 - 1, 'FF:FF')
        ]
        for domain_id, mac_address in mapping_id_mac_address:
            domain = Domain(domain_id, 'test', 1)
            first_mac_address = domain.mac_addresses[0]
            self.assertEqual(first_mac_address[:5], mac_address)
