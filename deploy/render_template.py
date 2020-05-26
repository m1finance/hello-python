#!/usr/local/bin/python3

import yaml
import os
from jinja2 import Template, Environment, FileSystemLoader

if __name__ == "__main__":
 config_data = yaml.load(open('./deploy/values.yml'))
 build_uid = '-'.join([os.environ['VERSION'], os.environ['CIRCLE_BUILD_NUM'], os.environ['CIRCLE_SHA1']])
 config_data["image"]["tag"]=build_uid
 config_data["chart"]["version"]=build_uid
 print(config_data)
 env = Environment(loader = FileSystemLoader('./templates'),   trim_blocks=True, lstrip_blocks=True)
 template = env.get_template('hello-python-hr.yml.j2')
 print(template.render(config_data))