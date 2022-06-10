#!/usr/bin/python3

import logging
import yaml

config_file = 'user_config.yaml'
# Load configuration
config = yaml.reader(config_file)
# Enter interactive mode