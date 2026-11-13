"""Check the native Light input; Rust format argument/type checks belong to its receiving build."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def catalog(path):
    value = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value, dict) or not all(isinstance(key, str) and isinstance(text, str) for key, text in value.items()):
        raise ValueError(f'{path}: a catalog must map strings to strings')
    return value

class NativeLightCatalogs(unittest.TestCase):
    def test_native_catalogs_are_paired_string_maps(self):
        directory = ROOT / 'app-catalogs/lightcraft/locales'
        files = sorted(directory.glob('*.json'))
        self.assertTrue(files, 'The native Light catalog input must not be empty')
        plain = {p.stem for p in files if not p.stem.endswith('-formats')}
        formatted = {p.stem.removesuffix('-formats') for p in files if p.stem.endswith('-formats')}
        self.assertEqual(plain, formatted)
        for path in files:
            with self.subTest(file=path.name):
                self.assertRegex(path.stem.removesuffix('-formats'), r'^[a-z]+(?:-[a-z]+)*$')
                self.assertTrue(catalog(path), 'A native catalog must not be empty')

if __name__ == '__main__':
    unittest.main()
