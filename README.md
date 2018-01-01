# Python True Block Weight

## Installation

```sh
pip3 install https://github.com/faustbrian/ARK-Python-Client/archive/master.zip
git clone https://github.com/galperins4/tbw
cd ~/tbw
npm install
```

## Configuration & Usage

After the repository has been cloned you need to open the `config.json` and change it to your liking. Once this has been done execute `python3 tbw.py` to start true block weight script.

Alternatively I have also included an apps.json file if you want to run tbw via PM2 (need to install PM2 first and then pm2 start apps.json)

Important! - pay_addresses and keep keys should match in config.json. DO NOT delete the reserve key as it is required. All other's can be deleted or more added

As the script leverages @FaustBrians ARK python client, python 3.6+ is required. In addition it is recommended to run this alongside an ark/kapu reiay node as inital api calls are made to localhost.


## To Do

- Add more features to config (e.g., tx fee handling, black/white list, etc)
- Add reserve balance check (to ensure if you are paying tx that fees <= reserve amt)
- Manual block processing / allocation
- Additional exception handling

## Changelog

### .03
- Modified config file to add minimum payment threshold functionality

### .02
- Modified config file and added multi-address capability for delegate share addresses

### .01
- Initial release

## Security

If you discover a security vulnerability within this package, please open an issue. All security vulnerabilities will be promptly addressed.

## Credits

- [galperins4](https://github.com/galperins4)
- [All Contributors](../../contributors)

## License

[MIT](LICENSE) © [galperins4](https://github.com/galperins4)





