# 何ができる？
結果の出力フォーマットを指定できる。
出力フォーマットに沿って、結果をパースできる。
pydanticを利用することで型まで指定ができる。

# メリット
出力をコントロールしやすい。

# ポイント
```
# 出力結果の型と型チェックを含めた定義
class SmartPhone(BaseModel):
    release_date: datetime.date = Field(description='スマホの発売日')
    screen_inches: float = Field(description='画面サイズ(インチ’)')
    os_installed: str = Field(description='スマホのOS')
    model_name: str = Field(description='モデル名')

    @field_validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError('screen inches must be a positive number')
        return field

parser=PydanticOutputParser(pydantic_object=SmartPhone)

# パースできなかった場合にLLMを用いて修正するようにラップできる。
output_parser = OutputFixingParser.from_llm(
    parser=PydanticOutputParser(pydantic_object=SmartPhone),
    llm=chat
)

# pydanticで定義したカラム名を.で扱える
    print(f'{parsed_result.model_name}')

```

