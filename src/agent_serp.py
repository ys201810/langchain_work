# -*- coding: utf-8 -*-
import pathlib
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.tools.file_management import WriteFileTool

import set_config


def main():
    base_path = pathlib.Path.cwd().parent
    yaml_file = base_path / 'config' / 'conf.yaml'
    config = set_config.run(yaml_file)

    chat = ChatOpenAI(model=config.get('openai_model_name', ''))
    tools = load_tools(
        ['requests_get', 'serpapi'],
        llm=chat
    )

    tools.append(WriteFileTool(root_dir='./'))
    agent = initialize_agent(
        tools,
        chat,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run('北海道の名産品を調べて、日本語でresult.txtというファイルに保存してください。')

    print(result)


if __name__ == '__main__':
    main()
