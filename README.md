# langchain_work
langchainを使って遊んでみる。

# 内容
- Output Parserを使って、出力結果を指定フォーマットで取得する。
- Redis(upstash)を用いて会話履歴を外部のKVSで保持して永続化する。

# コード
```
langchain_work/
  ┣src/
  ┃ ┣chat_memory_redis.py(Redisを使って会話履歴を永続化)
  ┃ ┣outout_parse_datetime.py(OutputParserでdatetime型の出力指定)
  ┃ ┣outout_parse_pydantic.py(Pydanticを使って出力指定)
  ┃ ┗outout_parse.py(OutputParserで,区切りのリストの出力指定)
  ┗docs/
    ┗上記のsrc/のコードに対応したメモファイル群
```

# 参考
- [LangChain完全入門　生成AIアプリケーション開発がはかどる大規模言語モデルの操り方](https://book.impress.co.jp/books/1123101047)
- [upstash](https://console.upstash.com/redis/fcea0328-b863-4fc5-aa01-bccaaf6686af)  
