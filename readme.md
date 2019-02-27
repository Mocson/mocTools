# pyTest
自分で試しに作っているものをアップしています。
不定期に更新をします。
動作確認はしていますが、作成途中のものも含まれますのでご注意ください。
現在は、PySideを学んでおります。

ダウンロードしたものは、pyTest以降をドキュメント内 mayaフォルダのscriptに配置してください。

## 配置Scriptフォルダ [XXXXX]はご自分のユーザー名に変えてください。

- windows
`C/Users/XXXXX/Documents/maya/scripts`
- macOS
`/Users/XXXXX/Library/Preferences/Autodesk/maya/scripts`

起動コマンド 例：keyframeBoxの起動
```python
from pyTest import keyFrameBox
reload(keyFrameBox)
keyFrameBox.main()
```

# keyFrameBox
キーフレームのコピーペーストをボタンでできるようにしたツールです。
