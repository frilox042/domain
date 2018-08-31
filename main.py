"""
Main
"""

from domain import Domain

NUM_MAC_ADDRESSES = 10


def main():
    """
    Main function
    """
    domain1: Domain = Domain(43690, 'D1', NUM_MAC_ADDRESSES)
    domain2: Domain = Domain(48059, 'D2', NUM_MAC_ADDRESSES)
    domain3: Domain = Domain(52428, 'D3', NUM_MAC_ADDRESSES)

    for domain in [domain1, domain2, domain3]:
        print(domain)

if __name__ == '__main__':
    main()
