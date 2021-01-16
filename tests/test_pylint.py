# Copyright (C) 2020 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# pylint: disable-all

import sys

from io import StringIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

from autohooks.config import load_config_from_pyproject_toml
from autohooks.terminal import Terminal
from autohooks.api import _set_terminal
from autohooks.api.git import Status, StatusEntry, get_staged_status

from autohooks.plugins.pylint.pylint import (
    DEFAULT_ARGUMENTS,
    DEFAULT_INCLUDE,
    check_pylint_installed,
    ensure_iterable,
    get_include_from_config,
    get_pylint_arguments,
    get_pylint_config,
    precommit,
)


def get_test_config_path(name):
    return Path(__file__).parent / name


class AutohooksPylintTestCase(TestCase):
    def test_pylint_installed(self):
        sys.modules['pylint'] = None
        with self.assertRaises(Exception):
            check_pylint_installed()

    def test_get_pylint_arguments(self):
        args = get_pylint_arguments(config=None)
        self.assertEqual(args, DEFAULT_ARGUMENTS)

    def test_get_pylint_config(self):
        config_path = get_test_config_path('pyproject.test.toml')
        self.assertTrue(config_path.is_file())

        autohooksconfig = load_config_from_pyproject_toml(config_path)
        self.assertTrue(autohooksconfig.has_config())

        pylint_config = get_pylint_config(autohooksconfig.get_config())
        self.assertEqual(pylint_config.get_value('foo'), 'bar')

    def test_ensure_iterable(self):
        foo = 'bar'  # pylint: disable=blacklisted-name
        bar = ensure_iterable(foo)  # pylint: disable=blacklisted-name
        self.assertEqual(bar, ['bar'])

        foo = ['bar']
        bar = ensure_iterable(foo)  # pylint: disable=blacklisted-name
        self.assertEqual(bar, ['bar'])

    def test_get_include_from_config(self):
        include = get_include_from_config(config=None)
        self.assertEqual(include, DEFAULT_INCLUDE)

    @patch('autohooks.plugins.pylint.pylint.ok')
    def test_precommit(self, _ok_mock):
        ret = precommit()
        self.assertFalse(ret)

    # these Terminal output functions don't run in the CI ...
    @patch('autohooks.plugins.pylint.pylint.ok')
    @patch('autohooks.plugins.pylint.pylint.out')
    @patch('autohooks.plugins.pylint.pylint.error')
    @patch('autohooks.plugins.pylint.pylint.get_staged_status')
    def test_precommit_staged(
        self, staged_mock, _error_mock, _out_mock, _ok_mock
    ):
        staged_mock.return_value = [
            StatusEntry(
                status_string='M  tests/lint_test.py',
                root_path=Path(__file__).parent,
            )
        ]
        ret = precommit()
        self.assertTrue(ret)
