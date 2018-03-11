- **pip**：パッケージインストールのためのツール。SwiftでいうところのPod

- **virtualenv**:パッケージを切り分ける仮想環境を作るツール。iOS開発でいうところのスキーム。
**プロジェクトごとにペッケージのバージョン依存関係を切り替えるのにはvirtualenvを使う**

- **venv**：Python3から公式として入ったvietualenv。ただし、現在はいろいろ不具合あるため使わないほうがよさそう

- **conda**：Continuumという会社が作っているPythonを中心とした科学計算のパッケージ管理をするためのプラットフォーム
- **pyenv**:Pythonのソースからのビルドと、Pythonの実行環境（バージョンなど）の切り替えをする

## これから始める人むけfor Mac　2018/03/11

### python3のインストール
```
brew install python3
```

### アップグレード
```
brew upgrade python
```

### ディレクトリ環境構築
```sh
python3 -m venv hoge
. hoge/bin/activate
python --version #ここで3~になっていればOK
```

### pip listでワーニングでるとき
pip.confを作成し、そこで設定を記述します。
Macの場合は、$HOME/Library/Application Support/pip/pip.conf
になりますが、ディレクトリ・ファイルがまだの場合は、作成します。

作成したファイルに次のように
[list]
format = <表示形式>
表示形式には、legacyやcolumns,freeze,jsonがあります。自分はcolumnsを選びました。

なお、ここで設定した場合は、全体に適用されます。virtualenvで個別に作りたい場合はvirtualenvのディレクトリ直下にpip.confを作って、設定してください。




##  参考URL
- https://medium.com/@chezou/python%E3%81%AE%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%82%92%E8%87%AA%E5%88%86%E3%81%AA%E3%82%8A%E3%81%AB%E6%95%B4%E7%90%86%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B-dc8d8f2fe989

- http://ymotongpoo.hatenablog.com/entry/2017/01/26/154124

- https://dev.classmethod.jp/server-side/language/pip-9-pip-list-deprecate-message/
