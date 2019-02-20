![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_logo_resilience_horizontal.png)

# autohooks-plugin-pylint

[![PyPI release](https://img.shields.io/pypi/v/autohooks-plugin-pylint.svg)](https://pypi.org/project/autohooks-plugin-pylint/)

An [autohooks](https://github.com/bjoernricks/autohooks) plugin for python code
linting via [pylint](https://github.com/PyCQA/pylint).

## Installation

### Install using pip

You can install the latest stable release of autohooks-plugin-pylint from the
Python Package Index using [pip](https://pip.pypa.io/):

    pip install autohooks-plugin-pylint

Note the `pip` refers to the Python 3 package manager. In environment where
Python 2 is also available the correct command may be `pip3`.

### Install using pipenv

It is highly encouraged to use [pipenv](https://github.com/pypa/pipenv) for
maintaining your project's dependencies. Normally autohooks-plugin-pylint is
installed as a development dependency.

    pipenv install --dev autohooks-plugin-pylint

## Usage

To activate the pylint autohooks plugin please add the following setting to your
*pyproject.toml* file.

```toml
[tool.autohooks]
pre-commit = ["autohooks.plugins.pylint"]
```

## Maintainer

This project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/bjoernricks/autohooks-plugin-pylint/pulls)
on GitHub. Bigger changes need to be discussed with the development team via the
[issues section at GitHub](https://github.com/bjoernricks/autohooks-plugin-pylint/issues)
first.

## License

Copyright (C) 2019 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
