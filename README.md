# marktree

![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)

Markdown ファイル（`.md`）の見出しをツリー形式で表示する CLI ツールです。

主な機能

* Markdown の見出し構造をツリー表示
* 指定した見出しレベルまで表示
* 見出しのみをプレーンテキストで出力
* クリップボードからMarkdownを入力
* 結果をクリップボードへ直接コピー
* UTF-8 / CP932 / Shift_JIS などの文字コードに対応

**English README**

https://github.com/yusu79/marktree/blob/main/README.en.md


<!-- omit in toc -->
## 目次

- [インストール](#インストール)
- [クイックスタート](#クイックスタート)
- [オプション](#オプション)
- [使用例](#使用例)
- [オプションの詳細](#オプションの詳細)
- [オプションの順序](#オプションの順序)
- [Windows でインストール時に警告が表示された場合](#windows-でインストール時に警告が表示された場合)
- [使用ライブラリ](#使用ライブラリ)
- [開発日記](#開発日記)


## インストール

```bash
pip install marktree
```

## クイックスタート

Markdown ファイル

```md
# h1

## h2

### h3

## h2

# h1
```

実行

```bash
marktree sample.md
```

出力

```text
├── h1
│  ├── h2
│  │  └── h3
│  └── h2
└── h1
```

## オプション

| コマンド                        | 説明                       |
| --------------------------- | ------------------------ |
| `marktree -h`               | ヘルプを表示                   |
| `marktree -L 3 file.md`     | 最大表示階層を指定                |
| `marktree -C`               | クリップボードから Markdown を読み込む |
| `marktree -P file.md`       | 見出しのみをプレーンテキストで出力        |
| `marktree -E cp932 file.md` | ファイルの文字コードを指定            |
| `marktree --copy file.md`   | 結果をクリップボードへコピー           |



## 使用例

### 通常の出力

```bash
marktree sample.md
```

```text
├── h1
│  ├── h2
│  │  └── h3
│  └── h2
└── h1
```

### 表示する階層を制限

```bash
marktree -L 2 sample.md
```

```text
├── h1
│  ├── h2
│  └── h2
└── h1
```


### クリップボードから入力

クリップボードにコピーした Markdown テキストを読み込みます。

```bash
marktree -C
```

`-L` オプションと組み合わせることもできます。

```bash
marktree -C -L 3
```


### 見出しのみを出力

```bash
marktree -P sample.md
```

出力

```text
# h1
## h2
### h3
## h2
# h1
```


### 結果をクリップボードへコピー

標準出力へ表示する代わりに、生成したツリーをクリップボードへコピーします。

```bash
marktree sample.md --copy
```


### 文字コードを指定

```bash
marktree -E cp932 sample.md
```

対応例

* utf-8
* cp932
* shift_jis


## オプションの詳細

### `-L`

表示する見出しレベルを指定します。

指定できる値は **1～6** です。

デフォルトは **6** です。


### `-C`

クリップボードにコピーされた Markdown テキストを入力として使用します。

ファイルを保存せずに構造を確認できます。


### `-P`

ツリー化せず、見出しのみをそのまま出力します。


### `-E`

Markdown ファイルを開く際の文字コードを指定します。

文字化けする場合はファイルの実際の文字コードを指定してください。

例

```bash
marktree -E cp932 sample.md
```

### `--copy`

標準出力へ表示する代わりに、生成した結果をクリップボードへ直接コピーします。



## オプションの順序

オプションの順序は自由です。

以下はどちらも同じ結果になります。

```bash
marktree -L 3 sample.md
```

```bash
marktree sample.md -L 3
```

複数の Markdown ファイルを指定した場合は、最後に指定したファイルを処理します。


## Windows でインストール時に警告が表示された場合

Windows 環境では、`pip install marktree` の実行時に以下のような警告が表示されることがあります。

### PATH に関する警告

```text
WARNING: The script xxx.exe is installed in '...' which is not on PATH.
```

これは、`marktree` コマンドの保存先に **PATH が設定されていない**場合に表示される警告です。

対処方法は、以下の記事をご参照ください。

https://yusu79.com/python-path-issue/



### インストールに失敗する警告

```text
WARNING: Failed to write executable - trying to use .deleteme logic
```

この警告が表示されて `pip install` が失敗する場合は、以下の記事をご参照ください。

https://yusu79.com/pip-install-failure-fix/



## 使用ライブラリ

* [pyperclip](https://github.com/asweigart/pyperclip)


## 開発日記

https://yusu79.com/dev-marktree/
