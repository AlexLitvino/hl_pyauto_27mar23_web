import configparser
import os


def get_project_dir():
    return os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]


def get_config():
    parser = configparser.ConfigParser()
    parser.read(os.path.join(get_project_dir(), 'config.ini'))
    return parser


def get_base_url():
    parser = get_config()
    return parser.get('testing', 'base_url')


def get_browser_name():
    parser = get_config()
    return parser.get('testing', 'browser_name')
