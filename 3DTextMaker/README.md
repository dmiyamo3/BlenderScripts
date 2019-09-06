# 3DTextMaker

入力したテキストを一文字毎分割してまとめてFBXファイルとして出力するblenderスクリプトです。

# 動作環境

 - blender2.8 β

# 使い方

1. blender を起動
1. cube を削除
1. メニューバーから「Scripting」へ移動
1. test.pyを開く
1. dirname（出力先フォルダ）とfontpath（フォントファイル）を適宜変更
1. テキストを自由に編集
1. パラメータを自由に変更（ bevel と remesh を使用する場合は isBevel, isRemeshをそれぞれ False から True に変更する）
1. 右クリックメニューから「スクリプト実行」
1. テキストが分割されたFBXファイルとして指定したフォルダに生成される

# 使用例

出力したファイルをUnityにインポートした例

<img src="https://pbs.twimg.com/media/EDswQDxVAAAqY9G?format=jpg&name=large" width="480">

ベベルなし、リメッシュなし

<img src="https://pbs.twimg.com/media/EDtQu6rU8AA1qsM?format=png&name=900x900" width="480">

ベベルあり、リメッシュなし

<img src="https://pbs.twimg.com/media/EDtQu6rU0AE-BiL?format=png&name=900x900" width="480">

ベベルなし、リメッシュあり

<img src="https://pbs.twimg.com/media/EDtQu6yUYAQm9HS?format=png&name=900x900" width="480">

ベベルあり、リメッシュあり


<img src="https://pbs.twimg.com/media/EDtQu6xUEAAmPa3?format=png&name=900x900" width="480">