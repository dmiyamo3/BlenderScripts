# 3DTextMaker

入力したテキストを一文字毎分割してまとめてFBXファイルとして出力するblenderアドオンです。

# 動作環境

 - blender2.8

# アドオンのインストール方法
1. 3DTextMakerAddOn.pyをダウンロード
1. メニューバーから「編集」->「プリファレンス」へ移動
1. 「インストール」ボタンからダウンロードした3DTextMakerAddOn.pyを選択してインストールする
1. 公式・コミュニティ・テスト中と並んでいるメニューの中から「テスト中」を選択
1. 3DTextMakerAddOnのチェックボックスを有効にする

# 使い方
1. ツールバーから「3DTextMaker」を開く
1. フォントのファイルを指定 (デフォルトはメイリオフォント)
1. テキスト入力 -> 「Create」ボタン -> 分割テキストを生成
1. 保存先フォルダを指定 -> 「Save」ボタン -> fbx形式で保存される

<img src="https://pbs.twimg.com/media/EGmJG7nUUAE6GIN?format=jpg&name=medium" width="480">


<br>
<br>
<br>


# 以下、旧バージョン(`test.py`)の説明

# 使い方

1. blender を起動
1. cube を削除
1. メニューバーから「Scripting」へ移動
1. test.pyを開き、編集する
    - dirname（出力先フォルダ）とfontpath（フォントファイル）を適宜変更
    - テキストを自由に編集
    - パラメータを自由に変更（ bevel と remesh を使用する場合は isBevel, isRemeshをそれぞれ False から True に変更する）
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

# CUIで使用する場合

1. test.pyの編集
    - dirname（出力先フォルダ）とfontpath（フォントファイル）を適宜変更
    - テキストを自由に編集
    - パラメータを自由に変更（ bevel と remesh を使用する場合は isBevel, isRemeshをそれぞれ False から True に変更する）
1. 以下を実行する

```
cd blender
blender --background --python C:/.../test.py
```