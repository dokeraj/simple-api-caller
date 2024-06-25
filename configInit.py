from dataclasses import dataclass
from typing import List
from typing import Optional

from dacite import from_dict

import yaml


@dataclass
class Header:
    key: Optional[str] = ''
    value: Optional[str] = ''


@dataclass
class Config:
    url: Optional[str] = ''
    http_method: Optional[str] = ''
    payload: Optional[str] = ''
    headers: Optional[List[Header]] = None
    converted_headers: Optional[dict[str, str]] = None


def populateHeadersForApi(config) -> Config:
    headerDict = {}
    if config.headers:
        for hed in config.headers:
            headerDict[hed["key"]] = hed["value"]

    config.converted_headers = headerDict
    return config


def validate_config(config: Config) -> None:
    if not config.url:
        print("Error: 'url' field is mandatory. Now Exiting!!")
        exit(1)
    if not config.http_method:
        print("Error: 'http_method' field is mandatory. Now Exiting!!")
        exit(1)
    if config.headers:
        for header in config.headers:
            dataclass_instance = from_dict(Header, header)
            if not dataclass_instance.key or not dataclass_instance.value:
                print("Error: Headers must have both 'key' and 'value'. Now Exiting!!")
                exit(1)


def read_yaml_file(file_path: str) -> List[Config]:
    try:
        with open(file_path, "r") as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return [Config(**item) for item in yaml_data]
    except FileNotFoundError:
        print(f"Error: YAML File '{file_path}' not found. Now exiting!")
        exit(1)


# Example usage
def initConfig() -> List[Config]:
    yaml_file_path = "/yaml/config.yml"
    configs = read_yaml_file(yaml_file_path)
    for config in configs:
        validate_config(config)
        populateHeadersForApi(config)
    return configs
