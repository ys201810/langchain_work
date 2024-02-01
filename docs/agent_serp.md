# 何ができる？
SERPAPIを用いて、Google検索した結果を利用できる。

# メリット
未学習のデータをGoogle検索を利用して追加できる。

# ポイント
```
# agentに持たせるtoolの定義。ここでserpapiの利用を指定。
tools = load_tools(
        ['requests_get', 'serpapi'],
        llm=chat
    )
    
# 得た結果を出力するパスの指定
tools.append(WriteFileTool(root_dir='./'))

# WriteFileToolを利用するために複数の入力が扱えるSTRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTIONを指定
agent = initialize_agent(
    tools,
    chat,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ファイルへの保存なども指定が可能
result = agent.run('北海道の名産品を調べて、日本語でresult.txtというファイルに保存してください。')
```

