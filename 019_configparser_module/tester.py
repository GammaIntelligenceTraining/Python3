from configparser import ConfigParser

config = ConfigParser()
config.read('config2.ini')


config.remove_section('EMAIL')
config.add_section('EMAIL')
config.set('EMAIL', 'login', 'roman123')
config.set('EMAIL', 'password', '123551')

with open('config2.ini', 'w') as configfile:
    config.write(configfile)