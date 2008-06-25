import sys, unittest, re, os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

def suite():
    tests = ['testCell']
    return unittest.TestSuite(map(CellTest, tests))

from SpiffWikiMarkup.Cell import Cell

class CellTest(unittest.TestCase):
    def testCell(self):
        cell = Cell()

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
