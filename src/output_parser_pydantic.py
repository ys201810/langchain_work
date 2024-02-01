# -*- coding: utf-8 -*-
import pathlib
from langchain import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser  # CommaSeparatedListOutputParser
from langchain_core.messages.human import HumanMessage
from pydantic import BaseModel, Field, validator
import datetime

import set_config


class SmartPhone(BaseModel):
    release_date: datetime.date = Field(description='スマホの発売日')
    screen_inches: float = Field(description='画面サイズ(インチ’)')
    os_installed: str = Field(description='スマホのOS')
    model_name: str = Field(description='モデル名')

    @validator("screen_inches")
    def validate_screen_inch(cls, field):
        if field <= 0:
            raise ValueError('screen inches must be a positive number')
        return field


def main():
    base_path = pathlib.Path.cwd().parent
    yaml_file = base_path / 'config' / 'conf.yaml'
    config = set_config.run(yaml_file)

    chat = ChatOpenAI(model=config['openai_model_name'])

    output_parser = OutputFixingParser.from_llm(
        parser=PydanticOutputParser(pydantic_object=SmartPhone),
        llm=chat
    )

    query = 'アンドロイドでリリースされたスマホを1つ挙げて'

    result = chat(
        [HumanMessage(content=query),
         HumanMessage(content=output_parser.get_format_instructions())]
    )  # resultの中身例：AIMessage(content='Ichiro Suzuki, Hideki Matsui, Hideo Nomo')

    parsed_result = output_parser.parse(result.content)
    print(f'query:{query}')
    print(f'{parsed_result}')
    print(f'{parsed_result.model_name}')


if __name__ == '__main__':
    main()
