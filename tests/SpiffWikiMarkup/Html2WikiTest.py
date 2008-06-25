import sys, unittest, re, os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

def suite():
    tests = ['testHtml2Wiki', 'testConvert']
    return unittest.TestSuite(map(Html2WikiTest, tests))

import os
from SpiffWikiMarkup import Html2Wiki, Wiki2Html

class Html2WikiTest(unittest.TestCase):
    def testHtml2Wiki(self):
        # Read the entire file into one string.
        filename = 'markup.txt'
        infile   = open(filename, 'r')
        in_str   = infile.read()
        infile.close()

        # Parse the file.
        parser = Html2Wiki()
        parser.feed('''<b>test</b>\n''')

        #print '"%s"' % parser.wiki
        self.assert_(parser.wiki == '''*test*''')


    def testConvert(self):
        # Read the entire file into one string.
        filename = 'markup.txt'
        infile   = open(filename, 'r')
        in_str   = infile.read()
        infile.close()

        # Convert Wiki to HTML.
        parser = Wiki2Html()
        parser.read(filename)
        html1 = parser.html
        #print html1

        # Convert the HTML back to Wiki.
        parser = Html2Wiki()
        parser.feed(html1)
        wiki = parser.wiki
        #print wiki

        # Write the wiki to a file.
        # The result contains an extra newline to mark a table end.
        # This is generally ok, but would break the unit test, so we
        # remove the last character before writing.
        fd = open(filename + '.tmp', 'w')
        fd.write(wiki[:-1])
        fd.close()

        # Convert the new Wiki file to HTML again.
        parser = Wiki2Html()
        parser.read(filename + '.tmp')
        html2 = parser.html
        #print html2

        # Clean up.
        os.remove(filename + '.tmp')

        # Make sure that the model is complete.
        self.assert_(len(in_str) > 10)
        self.assert_(len(html1)  > 10)
        self.assert_(html1 == html2)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
