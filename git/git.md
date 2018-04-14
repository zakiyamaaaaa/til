## PUSHするファイルサイズが50MB超える場合

５０MBを超えるファイルサイズの場合、PUSHしようとするとエラーが生じます。

この時git lfsを導入して解決します。

```
brew install git-lfs
```

->lfsを導入したいgitレポジトリに移動

```
git lfs install
```

ここでPUSHをするとまた失敗します。
Commitからやり直しましょう。
[commitをリセット]

```
git reset --soft ^HEAD
```

次に50MBを超えるファイルをlfsのトラックに登録しましょう。

```
git lfs [Track name]
```


できましたら、PUSHしましょう。



