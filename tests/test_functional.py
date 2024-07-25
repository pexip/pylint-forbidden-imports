"""Functional full-module tests for PyLint."""

from pathlib import Path

from pylint.testutils import LintModuleTest

try:
    from pylint.testutils.functional import FunctionalTestFile
except ImportError:
    from pylint.testutils.functional_test_file import FunctionalTestFile


TEST_DIR = Path(__file__).parent.resolve()


def test_import_recurse() -> None:
    test_file = FunctionalTestFile(TEST_DIR, "module1.py")
    lint_test = LintModuleTest(test_file)
    lint_test.setUp()
    lint_test.runTest()
