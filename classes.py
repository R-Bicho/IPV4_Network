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

    def validate_ip(self):
        ip_regexp = re.compile(
            r'^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if ip_regexp.search(self.ip):
            print('tem')
            return True
        else:
            print('Não tem')
            return False


if __name__ == '__main__':
    ipv4 = CalculateIPV4(ip='192.168.1.1/22')
