import sys
import os

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from test.PeleaTest import PeleaTest

if __name__ == "__main__":
  PeleaTest.tests()
  print("Tests passed")
