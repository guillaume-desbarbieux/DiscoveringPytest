from src.diamond import make_diamond

def test_a():
    resultat = make_diamond("A")
    assert resultat == "A"

def test_b():
    resultat = make_diamond("C")
    assert resultat == """
      A
     B B
    C   C
     B B
      A"""