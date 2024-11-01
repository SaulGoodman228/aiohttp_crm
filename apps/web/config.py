import typing
from dataclasses import dataclass

import yaml





@dataclass
class Config:
    username: str
    password: str


def setup_config(app):
    with open("config/config.yaml", "r") as f:
        raw_config = yaml.safe_load(f)

    app.config = Config(
        username=raw_config["credentials"]["username"],
        password=raw_config["credentials"]["password"],
    )
