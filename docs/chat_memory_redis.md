# 何ができる？
会話の履歴をもたせることができる。  
ConversationBufferMemoryでも可能だが、どんどん内部メモリを食っていく。
そこで外部にKVSのRedisを立てて無理ない履歴の保存をする。

# メリット
メモリを気にせず会話履歴を保持できる。

# ポイント
```
# RedisChatMessageHistryでupstashで作成したresisを利用するように指定。
history = RedisChatMessageHistory(
    session_id="chat_history",
    url=config.get('redis_url', ''),
)

# ConversationBufferMemoryのchat_memoryに、Redisから取得するhistoryを指定
memory = ConversationBufferMemory(
    return_messages=True,
    chat_memory=history,  # チャット履歴を指定
)

# ConversationChainで、memoryを用いてchatを指定。
chain = ConversationChain(
    memory=memory,
    llm=chat,
)
```

