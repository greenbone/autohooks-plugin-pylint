# Copyright (C) 2019-2022 Greenbone Networks GmbH
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
import sys

from autohooks.api import error, ok, out
from autohooks.api.git import get_staged_status, stash_unstaged_changes
from autohooks.api.path import match

DEFAULT_INCLUDE = ("*.py",)
DEFAULT_ARGUMENTS = ["--output-format=colorized"]


def check_pylint_installed():
    try:
        import pylint  # pylint: disable=import-outside-toplevel, disable=unused-import
    except ImportError as e:
        raise Exception(
            "Could not find pylint. Please add pylint to your python "
            "environment"
        ) from e


def get_pylint_config(config):
    return config.get("tool").get("autohooks").get("plugins").get("pylint")


def ensure_iterable(value):
    if isinstance(value, str):
        return [value]

    return value


def get_include_from_config(config):
    if not config:
        return DEFAULT_INCLUDE

    pylint_config = get_pylint_config(config)
    include = ensure_iterable(
        pylint_config.get_value("include", DEFAULT_INCLUDE)
    )

    return include


def get_pylint_arguments(config):
    if not config:
        return DEFAULT_ARGUMENTS

    pylint_config = get_pylint_config(config)
    arguments = ensure_iterable(
        pylint_config.get_value("arguments", DEFAULT_ARGUMENTS)
    )

    return arguments


def precommit(
    config=None, report_progress=None, **kwargs
):  # pylint: disable=unused-argument
    check_pylint_installed()

    include = get_include_from_config(config)

    files = [f for f in get_staged_status() if match(f.path, include)]

    if not files:
        ok("No staged files to lint.")
        return 0

    if report_progress:
        report_progress.init(len(files))

    arguments = get_pylint_arguments(config)

    with stash_unstaged_changes(files):
        ret = 0
        for f in files:
            cmd = ["pylint"]
            cmd.extend(arguments)
            cmd.append(str(f.absolute_path()))
            try:
                subprocess.run(cmd, check=True, capture_output=True)
            except subprocess.CalledProcessError as e:
                ret = e.returncode
                error(f"Linting error(s) found in {str(f.path)}:")
                lint_errors = (
                    e.stdout.decode(
                        encoding=sys.getdefaultencoding(), errors="replace"
                    )
                    .rstrip()
                    .split("\n")
                )
                # Skip the first line that only shows ******** Module blah
                for line in lint_errors[1:]:
                    out(line)

                continue
            finally:
                if report_progress:
                    report_progress.progress()

            ok(f"Linting {str(f.path)} was successful.")

        return ret
