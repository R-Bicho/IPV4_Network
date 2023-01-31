import re


class CalculateIPV4:
    '''receive the informations for calculate IPV4 network'''

    def __init__(self, ip=''):
        self.ip = ip

        if not self.validate_ip():
            raise ValueError('You need write only IP')

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
        prefix = value[1]
        return only_ip, prefix

    def ip_for_binary(self):
        '''Converted IP for binary value'''

        binary_ip = []

        only_ip, _ = self.separete_ip()
        ip_list = only_ip.split('.')

        for value in ip_list:
            temporary = bin(int(value))
            temporary = temporary[2:].zfill(8)
            binary_ip.append(temporary)
        return binary_ip

    def total_hosts(self):
        '''Calculated the total IPs on the network'''

        _, prefix = self.separete_ip()
        temporary = 32 - int(prefix)
        hosts = (2**temporary)
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

    def network_ip(self):
        '''Calculate decimal IP values to network'''

        values = self.ip_for_binary()
        _, prefix = self.separete_ip()
        bits_value_zero = '0' * (32 - int(prefix))

        string_bits = ''.join(values)
        string_bits_temporary = string_bits[0:int(prefix)]
        string_bits_temporary += bits_value_zero

        decimal_network_IP = []

        decimal_network_IP.append(
            str(int(string_bits_temporary[0:8], 2)))

        decimal_network_IP.append(
            str(int(string_bits_temporary[8:16], 2)))

        decimal_network_IP.append(
            str(int(string_bits_temporary[16:24], 2)))

        decimal_network_IP.append(
            str(int(string_bits_temporary[24:], 2)))

        string_network_IP = '.'.join(decimal_network_IP)
        return string_network_IP

    def Broadcast_ip(self):
        '''Calculate decimal IP values to brodcast'''

        values = self.ip_for_binary()
        _, prefix = self.separete_ip()
        bits_value_one = '1' * (32 - int(prefix))

        string_bits = ''.join(values)
        string_bits_temporary = string_bits[0:int(prefix)]
        string_bits_temporary += bits_value_one

        decimal_broadcast_IP = []

        decimal_broadcast_IP.append(
            str(int(string_bits_temporary[0:8], 2)))

        decimal_broadcast_IP.append(
            str(int(string_bits_temporary[8:16], 2)))

        decimal_broadcast_IP.append(
            str(int(string_bits_temporary[16:24], 2)))

        decimal_broadcast_IP.append(
            str(int(string_bits_temporary[24:], 2)))

        string_broadcast_IP = '.'.join(decimal_broadcast_IP)
        return string_broadcast_IP

    def __str__(self):
        return f'Calculation of the IPV4 network:\n'\
            f'\nIP: {self.separete_ip()[0]}'\
            f'\nPrefix: {self.separete_ip()[1]}'\
            f'\nNetwork Mask: {self.network_mask()}'\
            f'\nTotal IPs(Hosts): {self.total_hosts()}'\
            f'\nNetwork IP: {self.network_ip()}'\
            f'\nBroadcast IP: {self.Broadcast_ip()}'


if __name__ == '__main__':
    ipv4 = CalculateIPV4(ip='192.168.60.127/24')
    print(ipv4)
