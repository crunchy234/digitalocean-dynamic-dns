# DigitalOcean Dynamic DNS

This repository contains scripts for updating an A DNS record on DigitalOcean.

## Why is nothing working?

Try using python3 if you are not already. Also this script has only been tested on Linux.

Install python requirements: ```pip3 install -r requirements.txt```

Make sure you have a file in the root directory called ```digital_ocean_info.py```

An example of this file is:

```python
domain_name = "mydomain.com"
record_name = "vpn"
token = "54321abcdigitaloceantoken12345etc"
```

## Example Cron

The following will update the A record every 15 minutes.

```sh
# Update digitalocean public ip
*/15 * * * * python3 /path/to/repo/update_ip.py >> /var/log/digitalocean-update-ip.log
```

