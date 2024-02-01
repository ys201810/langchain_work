# 何ができる？
結果の出力フォーマットを指定できる。
出力フォーマットに沿って、結果をパースできる。

# メリット
出力をコントロールしやすい。

# ポイント
```
# 出力フォーマットの指定
output_parser = CommaSeparatedListOutputParser()

# プロンプトとして、フォーマットでの出力を指定
result = chat(
    [HumanMessage(content=query),
     HumanMessage(content=output_parser.get_format_instructions())]
)
# resultにはAIMessage(content='Ichiro Suzuki, Hideki Matsui, Hideo Nomo')のような値が入る。

# 指定した形式で結果をパース
output = output_parser.parse(result.content)
```

