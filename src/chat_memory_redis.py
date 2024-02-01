# -*- coding: utf-8 -*-
import pathlib
import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import RedisChatMessageHistory  # ← RedisChatMessageHistoryを追加
from langchain.memory import ConversationBufferMemory

import set_config


base_path = pathlib.Path.cwd().parent
yaml_file = base_path / 'config' / 'conf.yaml'
config = set_config.run(yaml_file)

chat = ChatOpenAI(model=config.get('openai_model_name', ''))

history = RedisChatMessageHistory(  # RedisChatMessageHistoryを初期化
    session_id="chat_history",
    url=config.get('redis_url', ''),  # 環境変数からRedisのURLを取得
)

memory = ConversationBufferMemory(
    return_messages=True,
    chat_memory=history,  # チャット履歴を指定
)

chain = ConversationChain(
    memory=memory,
    llm=chat,
)


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="私は会話の文脈を考慮した返答をできるチャットボットです。メッセージを入力してください。").send()


@cl.on_message
async def on_message(message: str):
    result = chain(message)

    await cl.Message(content=result["response"]).send()

"""
history = RedisChatMessageHistory(
    session_id='chat_history',
    url=config.get('redis_url', '')
)
memory = ConversationBufferMemory(
    return_messages=True,
    chat_memory=history
)
chain = ConversationChain(
    memory=memory,
    llm=chat
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content='チャットボットだよ！メッセージカモン！').send()

@cl.on_message
async def on_message(message: str):
    result = chain(message)

    await cl.Message(content=result["response"]).send()
"""

