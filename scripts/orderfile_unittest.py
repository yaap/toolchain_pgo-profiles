#!/usr/bin/env python3
#
# Copyright (C) 2019 The Android Open Source Project
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
# Sample Usage:
# $ python3 -m unittest orderfile_unittest.py

import os
import unittest
import subprocess

import create_orderfile
import utils

class TestCreateOrderfile(unittest.TestCase):
    top = utils.android_build_top()
    THIS_DIR = os.path.realpath(os.path.dirname(__file__))
    create_script = top+"/toolchain/pgo-profiles/scripts/create_orderfile.py"
    profile_file = top+"/toolchain/pgo-profiles/orderfiles/test/example.prof"
    mapping_file = top+"/toolchain/pgo-profiles/orderfiles/test/example-mapping.txt"
    denylist_file = top+"/toolchain/pgo-profiles/orderfiles/test/denylist.txt"
    output_file = THIS_DIR+"/default.orderfile"
    temp_file = THIS_DIR+"/temp.orderfile"

    # Test if the script creates an orderfile
    def test_create_orderfile_normal(self):
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file])
        self.assertTrue(os.path.isfile(self.output_file))

        # Clean up at the end
        os.remove(self.output_file)

    # Test if no mapping/profile file isn't passed then the script errors
    def test_create_orderfile_missing_mapping_argument(self):
        with self.assertRaises(subprocess.CalledProcessError) as context:
           utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file])

    # Test if the script creates an orderfile named temp.orderfile not default.orderfile
    def test_create_orderfile_output_name(self):
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file,
                            "--output", "temp.orderfile"])
        self.assertTrue(os.path.isfile(self.temp_file))
        self.assertFalse(os.path.isfile(self.output_file))

        # Clean up at the end
        os.remove(self.THIS_DIR+"/temp.orderfile")

    # Test if the script creates an orderfile by adding the leftover mapping symbols at the end of the orderfile
    def test_create_orderfile_leftover(self):
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file])
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file,
                            "--leftover",
                            "--output", "temp.orderfile"])

        self.assertTrue(os.path.isfile(self.temp_file))
        self.assertTrue(os.path.isfile(self.output_file))

        first  = []
        second = []
        with open(self.output_file, "r") as f:
            for line in f:
                first.append(line.strip())

        with open(self.temp_file, "r") as f:
            for line in f:
                second.append(line.strip())

        # Leftover flag will make the second orderfile either have the same
        # number of symbols or more than the first orderfile
        self.assertGreaterEqual(len(second), len(first))

        # Both orderfiles should have the same first few symbols
        for i in range(len(first)):
            self.assertEqual(first[i], second[i])

        # Clean up at the end
        os.remove(self.THIS_DIR+"/temp.orderfile")
        os.remove(self.output_file)

    # Test if the script creates an orderfile without main based on CSV format
    def test_create_orderfile_denylist(self):
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file,
                            "--denylist", "\"_Z4partPiii\""])

        self.assertTrue(os.path.isfile(self.output_file))

        with open(self.output_file, "r") as f:
            for line in f:
                line = line.strip()
                self.assertNotEqual(line, "_Z4partPiii")

        # Clean up at the end
        os.remove(self.output_file)

    # Test if the script creates an orderfile without main based on file format
    def test_create_orderfile_denylist(self):
        utils.check_call(["python3", self.create_script,
                            "--profile-file", self.profile_file,
                            "--mapping-file", self.mapping_file,
                            "--denylist", "@"+self.denylist_file])

        self.assertTrue(os.path.isfile(self.output_file))

        with open(self.output_file, "r") as f:
            for line in f:
                line = line.strip()
                self.assertNotEqual(line, "_Z4partPiii")

        # Clean up at the end
        os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()