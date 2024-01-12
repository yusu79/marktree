# marktree
![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dw/marktree)

Markdownファイル（.md）の見出しを木構造で表示するコマンドです。

<!-- omit in toc -->
## 目次（TOC）
- [インストール（Setup）](#インストールsetup)
- [使い方（Quick usage）](#使い方quick-usage)
- [解説（Usage）](#解説usage)
## インストール（Setup）
pipでインストールします。
```bash:
pip install marktree
```


### Windowsでのインストール手順

Windowsで`marktree`を`pip`を使用してインストールする際、`pip install`を実行した後に以下のような警告メッセージが表示されることがあります：

```powershell
WARNING: The script marktree.exe is installed in 'C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

この警告は、そのディレクトリがシステムの`PATH`に含まれていないことを示しています。この状態では、`python -m marktree`は実行されますが、`marktree`だけでは警告が表示されて実行できません。

これを解決するために、`Profile.ps1`に上記の`PATH`を追加してください：

```powershell
$env:path += ";C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts"
```



## 使い方（Quick usage）
```bash:
$ marktree [-h|--help] [-L|-l|--level 階層] [foo.md]
```

| オプション          | 説明                                                         | 
| ------------------ | ------------------------------------------------------------------ | 
| marktree -h        | ヘルプ画面を表示します。                                           | 
| marktree --help_jp | ヘルプ画面を日本語で表示します。                               | 
| marktree -L 3      | -Lオプションはツリーが表示される階層を決定します。 | 


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

## 解説（Usage）
`marktree`コマンドは、Markdownファイルの`#`に基づいてファイルをツリー階層として出力します。
`-L`オプションは元の`tree`コマンドと同様に深さを指定します。深さは1から6まで可能で、それ以上を指定するとエラーが発生しますので注意してください。

オプションの順序は、渡すMarkdownファイルを含めて特に決まっていません。
また、`markdown hoge.md hoge.md`のように複数のファイルを渡す場合、**最後のファイルのみ**が変換されて出力されます。
