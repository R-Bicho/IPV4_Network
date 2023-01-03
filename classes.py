import re


class CalculateIPV4:
    '''receive the informations for calculate IPV4 network'''

    def __init__(self, ip='', prefix='', mask='',
                 network='', broadcast='', number_ips=''):
        self.ip = ip
        self.prefix = prefix
        self.mask = mask
        self.network = network
        self.broadcast = broadcast
        self.number_ips = number_ips

        if self.validate_ip():
            pass
        else:
            raise ValueError('You need write only IP')

        self.network_mask()

    def validate_ip(self):
        '''checked if ip is correct'''

        ip_regexp = re.compile(
            r'^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if ip_regexp.search(self.ip):
            return True
        return False

    def separete_ip(self):
        '''ip section of prefix'''

        value = self.ip.split('/')
        only_ip = value[0]
        self.prefix = value[1]
        return only_ip, self.prefix

    def ip_for_binary(self):
        '''Converted IP for binary value'''

        only_ip, _ = self.separete_ip()
        remove_special_caracters = only_ip.split('.')
        new_ip = int(''.join(remove_special_caracters))
        binary_ip = bin(new_ip)
        return binary_ip[2:]

    def total_hosts(self):
        '''Calculated the total number of valid hosts on the network'''

        _, prefix = self.separete_ip()
        temporary = 32 - int(prefix)
        hosts = (2**temporary) - 2
        return hosts

    def network_mask(self):
        '''Calculated the sub-network mask'''

        _, prefix = self.separete_ip()
        bits_value_one = '1' * int(prefix)
        bits_value_zero = '0' * (32 - int(prefix))
        total_bits = bits_value_one + bits_value_zero

        separate_bits = []
        group_bits = []

        for value in total_bits:
            separate_bits.append(value)

        group_bits.append(''.join(separate_bits[0:8]))
        group_bits.append(''.join(separate_bits[8:16]))
        group_bits.append(''.join(separate_bits[16:24]))
        group_bits.append(''.join(separate_bits[24:]))

        temporary_mask = []
        for i in group_bits:
            temporary_mask.append(str(int(i, 2)))

        mask = '.'.join(temporary_mask)
        return mask


if __name__ == '__main__':
    ipv4 = CalculateIPV4(ip='192.168.1.1/22')
