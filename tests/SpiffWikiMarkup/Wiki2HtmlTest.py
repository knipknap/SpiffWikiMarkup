import sys, unittest, re, os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

def suite():
    tests = ['testWiki2Html', 'testConvert']
    return unittest.TestSuite(map(Wiki2HtmlTest, tests))

from Html2WikiTest   import Html2WikiTest
from SpiffWikiMarkup import Wiki2Html

class Wiki2HtmlTest(Html2WikiTest):
    def testWiki2Html(self):
        # Read the entire file into one string.
        filename = 'markup.txt'
        infile   = open(filename, 'r')
        in_str   = infile.read()
        infile.close()

        # Parse the file.
        parser = Wiki2Html()
        parser.read(filename)
        html = parser.html
        #print html

        # Now *that's* a poor test, huh? For a better test, look
        # at the test in Html2Wiki.py.
        self.assert_(len(html) > 1000)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
