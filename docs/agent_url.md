# 何ができる？
URLを指定して、そのテキストを読み込んで解答を得られる。

# メリット
未学習のデータをピンポイントで追加できる。

# ポイント
```
# 利用モジュール系。Agent系
from langchain.agents import AgentType, initialize_agent, load_tools

# agentに持たせるtoolの定義
tools = load_tools(
        ['requests'],
    )
# ツールを指定し、ZERO_SHOTでのレスポンスを指定。ReAct（REasoning and ACTing）で実行。
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 指定したURLへのアクセス指示
url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json'
result = agent.run(f'以下のURLにアクセスして東京の天気を調べ、日本語で答えてください。{url}')
```

