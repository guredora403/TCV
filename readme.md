# GUI Application Kit

wxPython を用いて音声読み上げ・弱視者向け表示設定に対応したアプリケーションを構築する際に便利なキット


## 環境構築

- シェル:コマンドプロンプトなど

- python 3.7 (3.8では動作しません)

-シェルから以下のコマンドを実行

	python -m pip install -r requirements.txt

.exeではなく.pyから実行する場合、一部機能を正しく実行するには.pyを *可変個引数を受け入れる形で* python.exeに関連付けしている必要がある。通常の関連付けではうまく動作しないので注意。

## 作成したソフトウェアの実行

python TCV.py  

## exeファイルにビルド

python tools\build.py

## 翻訳辞書ファイル(po)のアップデート

python tools\updateTranslation.py  

- locale フォルダを探索し、poファイルが自動配置される。

- 言語を追加したい場合は、locale フォルダに空フォルダを作ればよい。

- 前回の翻訳文は残ったままマージされるため、文字列が増えた場合も上記コマンドを利用すればよい。

## 翻訳したら  

python tools\buildTranslation.py

## 著作権

- 本キットの著作権はキット製作者にあるが、本キットを利用して制作されたアプリケーション、モジュール、拡張されたキット等について何らの権利も主張しない。
