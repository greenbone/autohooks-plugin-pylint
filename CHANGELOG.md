# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed

[Unreleased]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v21.6.0...HEAD


## [21.6.0] - 2021-06-13
### Changed
* Reworked file by file linting, improved the code and the tests. [#54](https://github.com/greenbone/autohooks-plugin-pylint/pull/54)

[21.6.0]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v20.11.0...v21.6.0

## [20.11.0] - 2020-11-09

### Added
* Adding pontos module for future releases [#24](https://github.com/greenbone/autohooks-plugin-pylint/pull/24)

### Changed

* Replaced pipenv with poetry for dependency management. poetry install works a bit different than pipenv install. It installs dev packages. [#16](https://github.com/greenbone/autohooks-plugin-pylint/pull/16)
* Linting file by file [#19](https://github.com/greenbone/autohooks-plugin-pylint/pull/19)

[20.11.0]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v1.2.0...v20.11.0

## [1.2.0] - 2019-11-22

### Added
* Allow to configure the arguments for pylint in *pyproject.toml* [#10](https://github.com/greenbone/autohooks-plugin-pylint/pull/10)

[1.2.0]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v1.1.1...v1.2.0

## [1.1.1] - 2019-09-13

### Fixed

* Don't run pylint if not files have to validates [#4](https://github.com/greenbone/autohooks-plugin-pylint/pull/4)

## [1.1.0] - 2019-03-28

### Changed

* Changed git repository location to https://github.com/greenbone/autohooks-plugin-pylint
* Allow to configure files to be linted [#1](https://github.com/greenbone/autohooks-plugin-pylint/pull/1)
* Use new autohooks status API to print messages [#1](https://github.com/greenbone/autohooks-plugin-pylint/pull/1)

[1.1.1]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/greenbone/autohooks-plugin-pylint/compare/v1.0.0...v1.1.0
