Question047 - 為什麼模組 simdjson 速度比較快 ? SIMD 到底是什麼 ?
=====
* ### 單指令多數據流 (SIMD, Single Instruction Multiple Data)
    * ### 以加法指令為例，單指令單數據 (SISD) 的 CPU 對加法指令解碼後，執行部件先訪問記憶體，取得第一個運算元；之後再一次訪問記憶體，取得第二個運算元；隨後才能進行求和運算。
    * ### 而在 SIMD 型的 CPU 中，指令解碼後幾個執行部件同時訪問記憶體，一次性獲得所有運算元進行運算。這個特點使 SIMD 特別適合於多媒體套用等數據密集型運算。
```
pip install pysimdjson
```
```
import simdjson

parser = simdjson.Parser()
doc = parser.parse(b'{"res": [{"name": "first"}, {"name": "second"}]}')

assert doc['res'][1]['name'] == 'second'
# True
assert doc.at_pointer('/res/1/name') == 'second'
# True
```
```
import simdjson


def main():
    # 创建 Parser 对象
    parser = simdjson.Parser()

    # 要解析的 JSON 字符串
    json_data = '{"key": "value", "array": [1, 2, 3]}'

    # 使用 parser.parse() 解析 JSON 数据
    doc = parser.parse(json_data)

    # 像访问字典一样访问解析后的 JSON 数据
    print(doc['key'])
    # 输出: value
    print(doc['array'][0])
    # 输出: 1


if __name__ == "__main__":
    main()
```
<br />
