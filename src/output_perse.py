# -*- coding: utf-8 -*-
import pathlib
from langchain_community.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage
# from langchain_core.messages.human import HumanMessage

import set_config


def main():
    base_path = pathlib.Path.cwd().parent
    yaml_file = base_path / 'config' / 'conf.yaml'
    config = set_config.run(yaml_file)

    output_parser = CommaSeparatedListOutputParser()

    chat = ChatOpenAI(model=config['openai_model_name'])

    query = '日本の代表的な野球選手を3名教えてください。'  # 'Appleが開発した代表的な製品を3つ教えてください。'
    result = chat(
        [HumanMessage(content=query),
         HumanMessage(content=output_parser.get_format_instructions())]
    )  # resultの中身例：AIMessage(content='Ichiro Suzuki, Hideki Matsui, Hideo Nomo')

    output = output_parser.parse(result.content)
    print(f'query:{query}')
    for item in output:
        print(f'結果:{item}')


if __name__ == '__main__':
    main()
