import pytest
from low_level_design.SOLID_Principle.liskov_substitution_principle.liskov_substitution import (
    Sparrow,
    Ostrich,
    describe_bird,
    describe_flyer,
    describe_walker,
)

'''
function and file must start with test_
class must start with Test
folder name doesn't need tp start with test_
'''

def test_sparrow_behaviors():
    sparrow = Sparrow()
    assert sparrow.eat() == "Sparrow eats seeds"
    assert sparrow.fly() == "Sparrow can fly"


def test_ostrich_behaviors():
    ostrich = Ostrich()
    assert ostrich.eat() == "Ostrich eats plants"
    assert ostrich.walk() == "Ostrich can walk"


def test_describe_bird_outputs(capsys):
    sparrow = Sparrow()
    ostrich = Ostrich()
    
    describe_bird(sparrow)
    describe_bird(ostrich)
    
    output,_ = capsys.readouterr()
    assert "Sparrow eats seeds" in output
    assert "Ostrich eats plants" in output


def test_describe_flyer_output(capsys):
    sparrow = Sparrow()
    describe_flyer(sparrow)
    captured = capsys.readouterr()

    assert "Sparrow can fly" in captured.out


def test_describe_walker_output(capsys):
    ostrich = Ostrich()
    describe_walker(ostrich)
    captured = capsys.readouterr()
    assert "Ostrich can walk" in captured.out
