# Changelog
すべての重要な変更はこのファイルに記録されます。

フォーマットは [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に基づき、
バージョニングは [Semantic Versioning](https://semver.org/lang/ja/) を採用しています。


---

## [1.2.0] - 2025-09-21
### Added
- `-e 文字コード` オプションでエンコードを指定可能に
- `-p` オプションで見出しをそのまま出力することが可能に

### Changed
- 内部コードをリファクタリング（ユーザー影響なし）

### Fixed
- `UnicodeDecodeError` が発生するケースを改善

---

## [1.0.0]
### Added
- 初回リリース
- Markdown 見出しをツリー表示する機能
