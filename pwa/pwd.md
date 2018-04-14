
1. まずhttps~じゃないとダメ。今回はgithubioで作る。もちろん無料

2. まず適当なindex.htmlファイルを作って、githubioのurlにアクセスして、httpsで表示されているか見てみる
https://自分のユーザ名.github.io

3. index.htmlと同じ階層にjsonファイルを置く。このjsonファイルでiconとかを設定する
- Googleによると192x192のpngアイコンが登録されていないとホーム画面に追加バナーがでないらしい
- 起動時のURL
- displayタイプをstandaloneに設定するとウェブアプリでブラウザUIを非表示にすることができる

4. Service Workerファイルを置く。index.htmlと同じ階層に。

5. index.htmlからmanifest.json,service-worker.jsを呼び出す

6. 上ファイルをmasterにpushすると、数秒後に反映される
- Webで確認したい場合は、chrome developer toolのapplicatioinにManifestという項目があり、そこから **"Add to homescreen"**をするとOK

## 参考URL

- https://qiita.com/umamichi/items/0e2b4b1c578e7335ba20