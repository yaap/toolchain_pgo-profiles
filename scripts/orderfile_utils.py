#!/usr/bin/env python
#
# Copyright (C) 2023 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def parse_set(param : str) -> set[str]:
    """Parse symbol set based on a file or comma-separate symbols."""
    symbol_set = set()
    if len(param) == 0:
        return symbol_set

    if param[0] == "@":
        with open(param[1:], "r") as f:
            for line in f:
                line = line.strip()
                symbol_set.add(line)
        return symbol_set

    list_symbols = param.split(",")
    symbol_set.update(list_symbols)
    return symbol_set

def parse_list(param : str) -> list[str]:
    """Parse partial order based on a file or comma-separate symbols."""
    symbol_order = []
    if len(param) == 0:
        return symbol_order

    if param[0] == "@":
        with open(param[1:], "r") as f:
            for line in f:
                line = line.strip()
                symbol_order.append(line)
        return symbol_order

    symbol_order = param.split(",")
    return symbol_order
