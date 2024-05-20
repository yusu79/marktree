# marktree

![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)

This command converts headings in a Markdown file (.md) into a tree-like structure and outputs it.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Setup](#setup)
- [Quick Usage](#quick-usage)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Dev-diary](#dev-diary)

## Setup
Install via pip:
```bash
pip install marktree
```

### Handling "Warning" on Windows
If you encounter a "`WARNING: The script clipcount.exe is installed in 'path' which is not on PATH.`" when running the above command on Windows, please refer to the following article.

Reference: [【Python Windows】pip install でPATHが通らない時の解決方法 | ゆすノート](https://yusu79.com/python-path-issue/)

If you see "`WARNING: Failed to write executable - trying to use .deleteme logic`", please refer to the following article:

Reference: [【Windows】警告が出て「pip install」できない時の解決方法 | ゆすノート](https://yusu79.com/pip-install-failure-fix/)


## Quick Usage
```bash
$ marktree [Options] [foo.md]
```


| Options            | Description                                                                                        | 
| ------------------ | -------------------------------------------------------------------------------------------------- | 
| marktree -h        | Display the help screen.                                                                           | 
| marktree --help_jp | Display the help screen in Japanese.                                                               | 
| marktree -L 3      | The -L option determines the level at which the tree is displayed.                                 | 
| marktree -C        | The -C option outputs the Markdown text copied to the clipboard directly in tree format. | 

### Example
Prepare the following Markdown named `foo.md`.
```md
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

- Regular output (default depth is 6):
```bash
$ marktree foo.md
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

- Use `-L 3` to determine the depth:
```bash
$ marktree -L 3 foo.md
├── h1 
│  ├── h2 
│  │  └── h3 
│  ├── h2 
│  └── h2
│     ├── h3 
│     └── h3
└── h1 
```
- Use `-C` outputs the Markdown text copied to the clipboard directly in tree format. Additionally, `-L` can be used in combination:
```bash
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


## Usage

The `marktree` command outputs the file as a tree hierarchy, depending on the `#` of the Markdown file. 
The `-L` option specifies the depth, as in the original `tree` command. Note that the depth can be from 1 to 6, and specifying more than that will result in an error.
The `-C` option outputs the Markdown text structure copied to the clipboard directly in tree format. This is convenient as it eliminates the need to copy the Markdown text to another file before outputting.

The order of the options is in no particular order, including the Markdown file to be passed. Also, if you pass multiple files like `markdown foo.md hoge.md`, **only the last file** will be converted and output.

## Dependencies
- [pyperclip](https://github.com/asweigart/pyperclip)

## Dev-diary
- [【個人開発】Markdownを木構造で出力できる「marktree」 | ゆすノート](https://yusu79.com/dev-marktree/)
