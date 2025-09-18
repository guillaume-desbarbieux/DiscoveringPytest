import pytest

from src.diamond import make_diamond

def test_a():
    resultat = make_diamond("A")
    assert resultat == "A"

def test_c():
    resultat = make_diamond("C")
    assert resultat == """  A
 B B
C   C
 B B
  A"""

def test_e():
    resultat = make_diamond("E")
    assert resultat == """    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A"""

@pytest.mark.skip
def test_z():
    resultat = make_diamond("Z")
    assert resultat ==  '                         A\n                        B B\n                       C   C\n                      D     D\n                     E       E\n                    F         F\n                   G           G\n                  H             H\n                 I               I\n                J                 J\n               K                   K\n              L                     L\n             M                       M\n            N                         N\n           O                           O\n          P                             P\n         Q                               Q\n        R                                 R\n       S                                   S\n      T                                     T\n     U                                       U\n    V                                         V\n   W                                           W\n  X                                             X\n Y                                               Y\nZ                                                 Z\n Y                                               Y\n  X                                             X\n   W                                           W\n    V                                         V\n     U                                       U\n      T                                     T\n       S                                   S\n        R                                 R\n         Q                               Q\n          P                             P\n           O                           O\n            N                         N\n             M                       M\n              L                     L\n               K                   K\n                J                 J\n                 I               I\n                  H             H\n                   G           G\n                    F         F\n                     E       E\n                      D     D\n                       C   C\n                        B B\n                         A' == '    A\n   B B\n  C   C\n D     D\nE       E\n D     D\n  C   C\n   B B\n    A'