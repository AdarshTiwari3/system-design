import pytest
from low_level_design.SOLID_Principle.interface_segregation_principle.interface_segregation import (NormalPrinter, MultiFunctionPrinter)

#reusable setup functions
# A fixture in pytest is a way to create reusable setup code for your test functions. It's used to prepare data or objects that will be used in one or more tests.

@pytest.fixture
def normal_printer() -> NormalPrinter:
    return NormalPrinter()

@pytest.fixture
def multi_function_printer() -> MultiFunctionPrinter:
    return MultiFunctionPrinter()


# ---------------------------
# NormalPrinter Tests
# ---------------------------

def test_normal_printer_supports_print_only(normal_printer):
    assert normal_printer.print() == "printing in progress..."
    
    # Ensure NormalPrinter does NOT have scan or fax
    with pytest.raises(AttributeError):
        normal_printer.scan()

    with pytest.raises(AttributeError):
        normal_printer.fax()


# ---------------------------
# MultiFunctionPrinter Tests
# ---------------------------

def test_multi_function_printer_print(multi_function_printer):
    assert multi_function_printer.print() == "printing in progress..."

def test_multi_function_printer_scan(multi_function_printer):
    assert multi_function_printer.scan() == "scanning in progress..."

def test_multi_function_printer_fax(multi_function_printer):
    assert multi_function_printer.fax() == "fax in progress..."