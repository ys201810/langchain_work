# -*- coding: utf-8 -*-
import pathlib
from langchain import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser # CommaSeparatedListOutputParser
from langchain_core.messages.human import HumanMessage

import set_config


def main():
    base_path = pathlib.Path.cwd().parent
    yaml_file = base_path / 'config' / 'conf.yaml'
    config = set_config.run(yaml_file)

    output_parser = DatetimeOutputParser()

    chat = ChatOpenAI(model=config['openai_model_name'])

    prompt = PromptTemplate.from_template('{product}のリリース日を教えて')
    prompt = prompt.format(product="プレイステーション2")

    result = chat(
        [HumanMessage(content=prompt),
         HumanMessage(content=output_parser.get_format_instructions())]
    )  # resultの中身例：AIMessage(content='Ichiro Suzuki, Hideki Matsui, Hideo Nomo')

    output = output_parser.parse(result.content)
    print(f'query:{prompt}')
    print(f'{output}')


if __name__ == '__main__':
    main()
