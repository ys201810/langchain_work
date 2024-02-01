# -*- coding: utf-8 -*-
import pathlib
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

import set_config


def main():
    base_path = pathlib.Path.cwd().parent
    yaml_file = base_path / 'config' / 'conf.yaml'
    config = set_config.run(yaml_file)

    chat = ChatOpenAI(model=config.get('openai_model_name', ''))
    tools = load_tools(
        ['requests'],
    )
    agent = initialize_agent(
        tools=tools,
        llm=chat,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json'
    result = agent.run(f'以下のURLにアクセスして東京の天気を調べ、日本語で答えてください。{url}')
    print(f'result:{result}')


if __name__ == '__main__':
    main()
