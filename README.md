![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_new-logo_horizontal_rgb_small.png)

# autohooks-plugin-pylint

[![PyPI release](https://img.shields.io/pypi/v/autohooks-plugin-pylint.svg)](https://pypi.org/project/autohooks-plugin-pylint/)

An [autohooks](https://github.com/greenbone/autohooks) plugin for python code
linting via [pylint](https://github.com/PyCQA/pylint).

## Installation

### Install using pip

You can install the latest stable release of autohooks-plugin-pylint from the
Python Package Index using [pip](https://pip.pypa.io/):

    pip install autohooks-plugin-pylint

Note the `pip` refers to the Python 3 package manager. In a environment where
Python 2 is also available the correct command may be `pip3`.

### Install using poetry

It is highly encouraged to use [poetry](https://python-poetry.org) for
maintaining your project's dependencies. Normally autohooks-plugin-pylint is
installed as a development dependency.

    poetry install

## Usage

To activate the pylint autohooks plugin please add the following setting to your
*pyproject.toml* file.

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pylint"]
```

By default, autohooks plugin pylint checks all files with a *.py* ending. If
only files in a sub-directory or files with different endings should be
formatted, just add the following setting:

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pylint"]

[tool.autohooks.plugins.pylint]
include = ['foo/*.py', '*.foo']
```

By default, autohooks plugin pylint executes pylint without any arguments and
pylint settings are loaded from the *.pylintrc* file in the root directory of
git repository. To change specific settings or to define a different pylint rc
file the following plugin configuration can be used:

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pylint"]

[tool.autohooks.plugins.pylint]
arguments = ["--rcfile=/path/to/pylintrc", "-s", "n"]
```

## Maintainer

This project is maintained by [Greenbone AG](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/greenbone/autohooks-plugin-pylint/pulls)
on GitHub. Bigger changes need to be discussed with the development team via the
[issues section at GitHub](https://github.com/greenbone/autohooks-plugin-pylint/issues)
first.

## License

Copyright (C) 2019 - 2022 [Greenbone AG](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
