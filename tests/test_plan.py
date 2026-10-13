# SPDX-License-Identifier: Apache-2.0
import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('validate', Path(__file__).resolve().parents[1] / 'tools/validate.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PlanningInvariants(unittest.TestCase):
    def test_current(self):
        module.validate(*module.load())

    def test_unqualified_claims_rejected(self):
        core, original = module.load()
        for key, bad in [('kernel', 'linux'), ('lunch', 'invented-userdebug'), ('status', 'supported'), ('blockers', [])]:
            with self.subTest(key=key):
                registry = copy.deepcopy(original)
                registry['targets'][0][key] = bad
                with self.assertRaises(ValueError):
                    module.validate(core, registry)

    def test_duplicate_rejected(self):
        core, registry = module.load()
        registry['targets'].append(copy.deepcopy(registry['targets'][0]))
        with self.assertRaises(ValueError):
            module.validate(core, registry)

    def test_moving_core_ref_rejected(self):
        core, registry = module.load()
        core['commit'] = 'main'
        with self.assertRaises(ValueError):
            module.validate(core, registry)
