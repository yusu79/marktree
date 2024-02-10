# marktree
![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)

Markdownファイル（.md）の見出しを木構造で表示するコマンドです。

[Read this in English.](https://github.com/yusu79/marktree/blob/main/README_en.md)

<!-- omit in toc -->
## 目次（TOC）
- [インストール（Setup）](#インストールsetup)
- [使い方（Quick usage）](#使い方quick-usage)
- [解説（Usage）](#解説usage)
- [使用しているパッケージ](#使用しているパッケージ)
## インストール（Setup）
pipでインストールします。
```bash:
pip install marktree
```

### Windowsで「警告」が出た時の対処方法

Windowsで上記のコマンドを実行した際に「警告（WARNING）」が表示されたなら、以下の記事を参照してください。

参考: [【Python Windows】pip install でPATHが通らない時の解決方法 | ゆすノート](https://yusu79.com/python-path-issue/)



## 使い方（Quick usage）
```bash:
$ marktree [オプション] [foo.md]
```

| オプション         | 説明                                                                                                    | 
| ------------------ | ------------------------------------------------------------------------------------------------------- | 
| marktree -h        | ヘルプ画面を表示します。                                                                                | 
| marktree --help_jp | ヘルプ画面を日本語で表示します。                                                                        | 
| marktree -L 3      | -Lオプションはツリーが表示される階層を決定します。                                                      | 
| marktree -C        | -Cオプションは、クリップボードにコピーされたMarkdownテキストをツリー形式で直接出力します。 | 


### 例
次のようなMarkdownファイル`hoge.md`を用意してください。
```md:
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



## 解説（Usage）
`marktree`コマンドは、Markdownファイルの`#`に基づいてファイルをツリー階層として出力します。
`-L`オプションは、元の`tree`コマンドと同様に深さを指定します。深さは1から6まで可能で、それ以上を指定するとエラーが発生しますので注意してください。
`-C`オプションは、クリップボードにコピーされたMarkdownテキストをツリー形式で直接出力します。これは出力前にMarkdownテキストを別のファイルにコピーする必要がなくなるので便利です。


オプションの順序は、渡すMarkdownファイルを含めて特に決まっていません。
また、`markdown hoge.md foo.md`のように複数のファイルを渡す場合、**最後のファイルのみ**が変換されて出力されます。

## 使用しているパッケージ
- [pyperclip](https://github.com/asweigart/pyperclip)
