# marktree
![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)

Markdownファイル（.md）の見出しを木構造で表示するコマンドです。

[Read this in English(英語版のREADMEはこちら)](https://github.com/yusu79/marktree/blob/main/README_en.md)

<!-- omit in toc -->
## 目次（TOC）
- [インストール（Setup）](#インストールsetup)
- [使い方（Quick usage）](#使い方quick-usage)
- [解説（Usage）](#解説usage)
- [使用しているパッケージ](#使用しているパッケージ)
- [開発日記(dev-diary)](#開発日記dev-diary)
## インストール（Setup）
pipでインストールします。
```bash:
pip install marktree
```

### Windowsで「警告」が出た時の対処方法

Windowsで上記のコマンドを実行した際に「`"WARNING: The script clipcount.exe is installed in 'ファイルパス' which is not on PATH."`」が表示されたなら、以下の記事をご参照ください。

参考: [【Python Windows】pip install でPATHが通らない時の解決方法 | ゆすノート](https://yusu79.com/python-path-issue/)

「`WARNING: Failed to write executable - trying to use .deleteme logic`」という警告が出て`pip install`が出来ない場合は、以下の記事をご参照ください。

参考: [【Windows】警告が出て「pip install」できない時の解決方法 | ゆすノート](https://yusu79.com/pip-install-failure-fix/)



## 使い方（Quick usage）
```bash:
$ marktree [オプション] [foo.md]
```

| オプション           | 説明                                                                                                    | 
| -------------------- | ------------------------------------------------------------------------------------------------------- | 
| marktree -h          | ヘルプ画面を表示します。                                                                                | 
| marktree --help-jp   | ヘルプ画面を日本語で表示します。                                                                        | 
| marktree -L 3        | -Lオプションはツリーが表示される階層を決定します。（デフォルト: 6）                                                      | 
| marktree -C          | -Cオプションは、クリップボードにコピーされたMarkdownテキストをツリー形式で直接出力します。           | 
| marktree -P          | -Pオプションを指定すると、ツリー化せずに見出しをそのまま出力します。                                    | 
| marktree -E 文字コード    | -Eオプションでファイルの文字コードを指定できます（例: utf-8, cp932, shift_jis）。「Decode Failed」というエラーが出たら使用してください（デフォルト: utf-8 ）                      |


### 例
次のようなMarkdownファイル`hoge.md`を用意してください。
```md:
# h1
ここではセクション全体の概要を紹介します。読者がこの章で何を学べるかを簡単に説明します。

## h2
最初のトピックについて詳しく説明します。背景や前提条件もここで示します。

### h3
この小節では、上で紹介したトピックに関する具体的な詳細を述べます。

#### h4
さらに理解を深めるための補足情報や注意点をここに記載します。

#### h4
追加の例やポイントを挙げて、前の小節の内容を補強します。

## h2
このセクションでは、二つ目の主要なポイントを紹介し、関連情報を提供します。

## h2
別の重要なトピックについて説明し、例や考察を加えます。

### h3
二つ目のトピックに関する詳細を掘り下げ、重要な概念を解説します。

#### h4
具体的な使用例やケーススタディを示し、理解を助けます。

##### h5
補足的なポイントや注意事項を挙げ、主要な議論をサポートします。

###### h6
参考情報や注釈、追加のヒントなど、詳細情報を提供します。

### h3
この小節の結論として、重要なポイントをまとめます。

# h1
最後のセクションでは全体のまとめを行い、読者への締めくくりを提供します。

``` 

- 通常の出力（デフォルトの階層は6）:
```
$ marktree hoge.md
├── h1 
│  ├── h2 
│  │  └── h3 
│  │     ├── h4 
│  │     └── h4 
│  ├── h2 
│  └── h2
│     ├── h3 
│     │  └── h4 
│     │     └── h5 
│     │        └── h6 
│     └── h3
└── h1 
```

- `-L 3`を使用して階層を決める:
```
$ marktree -L 3 hoge.md
├── h1 
│  ├── h2 
│  │  └── h3 
│  ├── h2 
│  └── h2
│     ├── h3 
│     └── h3
└── h1 
```
- `-C`を使用すると、クリップボードにコピーされたMarkdownテキストをツリー形式で直接出力します。さらに、`-L`を組み合わせて使うこともできます:
```
$ marktree -C -L 3 
├── h1 
│  ├── h2 
│  │  └── h3 
│  ├── h2 
│  └── h2
│     ├── h3 
│     └── h3
└── h1 
```

- `-P`を使用すると、見出しをそのまま出力します。文章の見出しだけ取得したい場合に、ご使用ください:
```
$ marktree -C -P 
# h1
## h2
### h3
#### h4
#### h4
## h2
## h2
### h3
#### h4
##### h5
###### h6
### h3
# h1
```



## 解説（Usage）
`marktree` コマンドは、Markdown ファイルの `#` に基づいてファイルをツリー階層として出力します。

* `-L` オプションは、元の `tree` コマンドと同様に出力の深さを指定します。深さは 1 から 6 まで可能で、それ以上を指定するとエラーが発生しますので注意してください。（デフォルト: 6）
* `-C` オプションは、クリップボードにコピーされた Markdown テキストをツリー形式で直接出力します。これにより、Markdown テキストを別ファイルにコピーする必要がなくなります。
* `-P` オプションを指定すると、ツリー化せずに見出しをそのまま出力します。ツリー構造ではなく平文で見出しだけ確認したい場合に便利です。
* `-E` オプションでは、ファイルを開く際の文字コードを指定できます（例: `utf-8`、`cp932`、`shift_jis`）。文字化けを防ぐため、ファイルの実際の文字コードに合わせて指定してください。（デフォルト: `utf-8`）

オプションの順序は、渡す Markdown ファイルを含めて特に決まっていません。
また、複数のファイルを渡した場合（例: `markdown hoge.md foo.md`）、**最後に指定したファイルのみ**が変換されて出力されます。


## 使用しているパッケージ
- [pyperclip](https://github.com/asweigart/pyperclip)

## 開発日記(dev-diary)
- [【個人開発】Markdownを木構造で出力できる「marktree」 | ゆすノート](https://yusu79.com/dev-marktree/)
