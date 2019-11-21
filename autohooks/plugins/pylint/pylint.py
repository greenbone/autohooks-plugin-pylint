# Copyright (C) 2019 Greenbone Networks GmbH
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

import subprocess

from autohooks.api import ok, fail
from autohooks.api.path import match
from autohooks.api.git import get_staged_status, stash_unstaged_changes

DEFAULT_INCLUDE = ('*.py',)
DEFAULT_ARGUMENTS = []


def check_pylint_installed():
    try:
        import pylint  # pylint: disable=import-outside-toplevel
    except ImportError:
        raise Exception(
            'Could not find pylint. Please add pylint to your python '
            'environment'
        )


def get_pylint_config(config):
    return config.get('tool').get('autohooks').get('plugins').get('pylint')


def ensure_iterable(value):
    if isinstance(value, str):
        return [value]

    return value


def get_include_from_config(config):
    if not config:
        return DEFAULT_INCLUDE

    pylint_config = get_pylint_config(config)
    include = ensure_iterable(
        pylint_config.get_value('include', DEFAULT_INCLUDE)
    )

    return include


def get_pylint_arguments(config):
    if not config:
        return DEFAULT_ARGUMENTS

    pylint_config = get_pylint_config(config)
    arguments = ensure_iterable(
        pylint_config.get_value('arguments', DEFAULT_ARGUMENTS)
    )

    return arguments


def precommit(config=None, **kwargs):  # pylint: disable=unused-argument
    check_pylint_installed()

    include = get_include_from_config(config)
    files = [f for f in get_staged_status() if match(f.path, include)]

    if not files:
        ok('No staged files to lint.')
        return 0

    arguments = get_pylint_arguments(config)

    with stash_unstaged_changes(files):
        args = ['pylint']
        args.extend(arguments)
        args.extend([str(f.absolute_path()) for f in files])

        status = subprocess.call(args)
        str_files = ', '.join([str(f.path) for f in files])

        if status:
            fail('Linting error(s) found in {}.'.format(str_files))
        else:
            ok('Linting {} was successful.'.format(str_files))

        return status
