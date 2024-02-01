# -*- coding: utf-8 -*-
import os
import yaml


def run(yaml_path: str):
    with open(yaml_path, "r") as f:
        config = yaml.safe_load(f)
    config = {
        'openai_key': config['openai_key'],
        'openai_model_name': config['openai_model_name'],
        'redis_url': config['redis_url'],
        'serp_api_key': config['serp_api_key']
    }
    os.environ["OPENAI_API_KEY"] = config['openai_key']
    os.environ["SERPAPI_API_KEY"] = config['serp_api_key']
    return config

