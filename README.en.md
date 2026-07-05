# marktree

![GitHub License](https://img.shields.io/github/license/yusu79/marktree)
![PyPI - Version](https://img.shields.io/pypi/v/marktree)
![PyPI - Downloads](https://img.shields.io/pypi/dm/marktree)

A CLI tool that displays the headings of a Markdown (`.md`) file as a tree structure.

Features

- Display Markdown heading hierarchy as a tree
- Limit the maximum heading level
- Output headings as plain text
- Read Markdown directly from the clipboard
- Copy the generated result to the clipboard
- Support UTF-8, CP932, Shift_JIS and other encodings

**Japanese README**

https://github.com/yusu79/marktree/blob/main/README.md

<!-- omit in toc -->
## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Options](#options)
- [Examples](#examples)
- [Option Details](#option-details)
- [Option Order](#option-order)
- [Windows Installation Warnings](#windows-installation-warnings)
- [Dependencies](#dependencies)
- [Development Diary](#development-diary)


## Installation

```bash
pip install marktree
```

## Quick Start

Markdown file:

```md
# h1

## h2

### h3

## h2

# h1
```

Run:

```bash
marktree sample.md
```

Output:

```text
├── h1
│  ├── h2
│  │  └── h3
│  └── h2
└── h1
```

## Options

| Command | Description |
| --- | --- |
| `marktree -h` | Show help |
| `marktree -L 3 file.md` | Limit the maximum heading level |
| `marktree -C` | Read Markdown from the clipboard |
| `marktree -P file.md` | Output headings as plain text |
| `marktree -E cp932 file.md` | Specify the file encoding |
| `marktree --copy file.md` | Copy the result to the clipboard |

## Examples

### Default Output

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

### Limit the Heading Level

```bash
marktree -L 2 sample.md
```

```text
├── h1
│  ├── h2
│  └── h2
└── h1
```

### Read from the Clipboard

Reads the Markdown text currently stored in the clipboard.

```bash
marktree -C
```

You can combine it with the `-L` option.

```bash
marktree -C -L 3
```

### Output Headings Only

```bash
marktree -P sample.md
```

Output:

```text
# h1
## h2
### h3
## h2
# h1
```

### Copy the Result to the Clipboard

Copies the generated tree to the clipboard instead of printing it to standard output.

```bash
marktree sample.md --copy
```

### Specify the File Encoding

```bash
marktree -E cp932 sample.md
```

Supported examples:

* utf-8
* cp932
* shift_jis

## Option Details

### `-L`

Displays headings up to the specified level. Valid values are **1–6** (default: **6**).

### `-C`

Uses the Markdown text currently stored in the clipboard as input.

This allows you to view the heading structure without saving the text to a file.

### `-P`

Outputs only the headings without tree formatting.

### `-E`

Specifies the file encoding, for example:

```bash
marktree -E cp932 sample.md
```

### `--copy`

Copies the generated output to the clipboard instead of printing it to standard output.

## Option Order

Options can be specified in any order.

```bash
marktree -L 3 sample.md
```

```bash
marktree sample.md -L 3
```

If multiple Markdown files are specified, only the last one is processed.

## Windows Installation Warnings

If you see:

```text
WARNING: The script xxx.exe is installed in '...' which is not on PATH.
```

See:

https://yusu79.com/python-path-issue/

If you see:

```text
WARNING: Failed to write executable - trying to use .deleteme logic
```

See:

https://yusu79.com/pip-install-failure-fix/

## Dependencies

- [pyperclip](https://github.com/asweigart/pyperclip)

## Development Diary

https://yusu79.com/dev-marktree/
