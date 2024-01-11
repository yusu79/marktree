# marktree
![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)


This command converts headings in a Markdown file (.md) into a tree-like structure and outputs it.

[日本語のREADMEはこちらから。](https://github.com/yusu79/marktree/blob/main/README_jp.md)

<!-- omit in toc -->
## TOC
- [Setup](#setup)
- [Quick usage](#quick-usage)
- [Usage](#usage)
## Setup
Install via pip:
```bash:
pip install marktree
```

## Quick usage
```python:
marktree [-h|--help] [-L|-l|--level level] [foo.md]
```

| options            | description                                                        | 
| ------------------ | ------------------------------------------------------------------ | 
| marktree -h        | Display the help screen.                                           | 
| marktree --help_jp | Display the help screen in Japanese.                               | 
| marktree -L 3      | The -L option determines the level at which the tree is displayed. | 


### Example
Prepare the following Markdown named `foo.md`.
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

- Regular output (default depth is 6).
```
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

- Use `-L 3` to determine the depth.
```
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



## Usage

The `marktree` command outputs the file as a tree hierarchy, depending on the `#` of the Markdown file.
The `-L` option specifies the depth, as in the original `tree` command. Note that the depth can be from 1 to 6, and specifying more than that will result in an error.

The order of the options is in no particular order, including the Markdown file to be passed.
Also, if you pass multiple files like `markdown foo.md hoge.md`, **only the last file** will be converted and output.
