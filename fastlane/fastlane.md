
2018/04/01

### fastlane testをやろうとしたらnot found となった

下記コマンドを打ってみる。
失敗。

```
export GEM_HOME=~/.gems
export PATH=$PATH:~/.gems/bin
```

それでもfastlaneコマンドがきかなかったので、素直にsudo bundle install fastlane,で再度入れ直してみる。

そんでfastlane testを打ってみる

~~Appstoreに提出用のスクリーンショットをとってくれるらしい。どの画面のスクリーンショットをとってくれるのだろう。~~
→Testを実行してくれる。結果については、Slackのwebhookを設定していたら、通知が来る


やってみたら、エラーがでた。

```
Unable to boot device due to insufficient system resources.
```

どうやらシミュレータを起動するのに十分なりソースがない、とのこと。

そんでぐぐると次のコマンドで制限をあげるらしい

```
sudo launchctl limit maxproc 2000 2500
```
そんでもっかいfastlane testやって、成功した。


### ベータ版のアップロード

Fastfileに次のように書く

```
lane :beta do
  # Adjust the `build_type` and `flavor` params as needed to build the right APK for your setup
  gradle(
    task: 'assemble',
    build_type: 'Release'
  )

  # ...
end
```

そんで、fastlane betaを打つ。

途中↓のメッセージがでる

```
Build doesn't show up in the build list anymore, waiting for it to appear again (check your email for processing issues if this continues)
```

何やらビルドが上がってこないので、emailチェックしてみろと。
emial探すも出てこない。。。
itunesconnectのアクティビティを見てみると、ビルドはあがってるみたい。。。

そんで、もっかいログを見てみると、成功したメッセージが。なんなんだ。。。

ちなみにfastlaneコマンドを打ってからビルドしてアップされるまで27分かかりました。





