#! /usr/bin/env python3
import datetime
import os

# noinspection PyPackageRequirements
import digitalocean
import subprocess

try:
    import digital_ocean_info
    trash = digital_ocean_info.domain_name
    trash = digital_ocean_info.record_name
    trash = digital_ocean_info.token
except ImportError or AttributeError:
    # noinspection SpellCheckingInspection
    print('Please make sure you have a file called "digital_ocean_info.py"\n'
          'With a variable the string variables: domain_name, record_name, and token \n'
          'Example:\n'
          'domain_name = "mydomain.com"',
          'record_name = "vpn"',
          'token = "54321abcdigitaloceantoken12345etc"')
    digital_ocean_info = 'keeping pycharm happy :)'
    exit(1)

domain = digitalocean.Domain(token=digital_ocean_info.token,
                             name=digital_ocean_info.domain_name)

records = domain.get_records()
dir_path = os.path.dirname(os.path.realpath(__file__))

res = subprocess.check_output([os.path.join(dir_path, 'get_ip.sh')])
external_ip = res.decode('utf-8').replace('"', '').replace('\n', '')

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print('my external ip: {0}'.format(external_ip))

for record in records:
    if record.name == digital_ocean_info.record_name:
        print('current ip in record: {0}'.format(record.data))
        record.data = external_ip
        record.save()
        break

print('\n')
