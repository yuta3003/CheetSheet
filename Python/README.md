# Python

## 特定行から文字列抽出

```python
for covid19_case in covid19_cases:
    # print(covid19_case.text)
    # print(re.search(r'\（.+?\）', covid19_case.text).text)    # 抽出
    target_day = re.sub(r'.+?\（', "（", covid19_case.text)     # 置換
    # print(type(target_day))
```