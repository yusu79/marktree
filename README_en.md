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

If you encounter a "`WARNING: The script clipcount.exe is installed in 'path' which is not on PATH.`" when running the above command on Windows, please refer to the following article:

Reference: [【Python Windows】pip install でPATHが通らない時の解決方法 | ゆすノート](https://yusu79.com/python-path-issue/)

If you see "`WARNING: Failed to write executable - trying to use .deleteme logic`", please refer to the following article:

Reference: [【Windows】警告が出て「pip install」できない時の解決方法 | ゆすノート](https://yusu79.com/pip-install-failure-fix/)

## Quick Usage

```bash
$ marktree [Options] [foo.md]
```

| Options             | Description                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| marktree -h         | Display the help screen.                                                                                                       |
| marktree --help-jp | Display the help screen in Japanese.                                                                                           |
| marktree -L 3       | Determines the depth at which the tree is displayed (default: 6).                                                              |
| marktree -C         | Outputs the Markdown text copied to the clipboard directly in tree format.                                                     |
| marktree -P         | Outputs only the headings without tree formatting (plain view).                                                                |
| marktree -E <enc>   | Specifies the file encoding (example: utf-8, cp932, shift\_jis). Use this if you get a "Decode Failed" error (default: utf-8). |

### Example

Prepare the following Markdown file `foo.md`:

```md
# h1
This is an introduction paragraph under h1. It gives an overview of the section.

## h2
Here we discuss the first topic in detail, providing some context and background.

### h3
This subsection contains more specific details about the topic introduced above.

#### h4
Additional notes and clarifications are provided here to help understand the subtopic.

#### h4
Another set of points and examples relevant to this sub-subsection.

## h2
The second main point of this section is introduced here with supporting information.

## h2
This section explains another topic of equal importance, with examples and discussion.

### h3
A deeper dive into the details of the second topic, explaining key concepts.

#### h4
Specific use cases and examples are provided here to clarify the points above.

##### h5
Minor subpoints or notes that are relevant but not central to the discussion.

###### h6
Detailed footnotes, references, or additional tips can be added here for completeness.

### h3
Concluding remarks for this subsection, summarizing key takeaways.

# h1
Final section summarizing the overall content and providing closure.

```

* Regular output (default depth is 6):

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

* Using `-L 3` to limit depth:

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

* Using `-C` to read from clipboard directly (can combine with `-L`):

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

* Using `-P` to output headings only:

```bash
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

## Usage

The `marktree` command outputs the file as a tree hierarchy based on the `#` headings in the Markdown file.

* The `-L` option specifies the output depth, similar to the original `tree` command. Depth can be from 1 to 6; specifying more than that will result in an error (default: 6).
* The `-C` option outputs Markdown text copied to the clipboard directly in tree format. This eliminates the need to copy the Markdown text to another file before outputting.
* The `-P` option outputs headings in plain format without tree formatting. Use this if you only want the headings.
* The `-E` option allows you to specify the file encoding (examples: `utf-8`, `cp932`, `shift_jis`). Use this if you encounter a "Decode Failed" error (default: `utf-8`).

The order of options is flexible, including the Markdown file to be processed. If multiple files are provided (e.g., `markdown foo.md hoge.md`), **only the last file** will be converted and output.

## Dependencies

* [pyperclip](https://github.com/asweigart/pyperclip)

## Dev-diary

* [Personal development: Creating "marktree" to output Markdown as tree | ゆすノート](https://yusu79.com/dev-marktree/)
