"""
Domain Class
"""

from typing import Iterator, List

MAC_ADDRESS_SEPARATOR_SIZE = 2
MAC_ADDRESS_SIZE = 12


def simple_mac_generator(length: int = 8) -> Iterator[str]:
    """
    Simple mac address generator
    :param length: the length of the generated mac address
    :return: A generator of the right length
    """
    i: int = 0
    formater: str = '{:0' + str(length) + 'x}'
    while True:
        yield formater.format(i)
        i += 1


class Domain():
    """
    Domain
    """

    def __init__(self,
                 id: int,  # pylint: disable=invalid-name,redefined-builtin
                 name: str,
                 num_mac_addresses: int = 0,
                 address_generator: Iterator[str] = simple_mac_generator(),
                ) -> None:
        """
        Domain contructor
        :param id: id of the domain
        :param name: name of the domain
        :param address_generator: unique mac addresses generator
        :param num_mac_addresses: number of mac addresses to populate
        :return: Domain
        """
        self.id: int = id  # pylint: disable=invalid-name
        self.name: str = name
        self.address_generator = address_generator
        self.mac_addresses: List[str] = [self._generate_mac_addresses()
                                         for _ in range(num_mac_addresses)]

    def _generate_mac_addresses(self) -> str:
        """
        Generate mac addresses according to id and address_generator
        :return: mac address
        """
        mac_identifier: str = '{:04x}'.format(self.id)
        mac_tail: str = next(self.address_generator)
        mac_id_tail: str = (mac_identifier + mac_tail)[:MAC_ADDRESS_SIZE]
        mac_iterator: Iterator[str] = iter(mac_id_tail)
        double_iterator: List[Iterator[str]] = (
            [mac_iterator] * MAC_ADDRESS_SEPARATOR_SIZE)
        group_by_2: Iterator[str] = map(''.join,
                         zip(*double_iterator))
        return ':'.join(group_by_2).upper()

    def __repr__(self) -> str:
        """
        Representation of Domain
        :return: string representing Domain
        """
        return '<ID: {}, Name: "{}", Mac addresses: [{}]>'.format(
            self.id,
            self.name,
            ', '.join(['"' + mac_address + '"'
                       for mac_address in self.mac_addresses])
        )
