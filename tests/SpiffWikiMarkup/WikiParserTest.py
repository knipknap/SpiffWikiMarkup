import sys, unittest, re, os.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

def suite():
    tests = ['testWikiParser']
    return unittest.TestSuite(map(WikiParserTest, tests))

from SpiffWikiMarkup.WikiParser import WikiParser

class WikiParserTest(unittest.TestCase):
    def testWikiParser(self):
        # Read the entire file into one string.
        filename  = 'markup.txt'
        infile    = open(filename, "U")
        in_text   = infile.read()
        infile.close()

        # Re-open and parse the entire file.
        infile  = open(filename, "r")
        scanner = WikiParser(infile, filename)
        content = ''
        nonecount = 0
        while True:
            token    = scanner.read()
            position = scanner.position()
            if token[0] is None:
                nonecount += 1  # This is because Plex is broken.
            if nonecount >= 2:
                break
            #print "Token type: %s, Token: '%s'" % (token[0], token[1])
            if not token[0] in ['indent', 'dedent']:
                content += token[1]

        # Make sure that every single string was extracted.
        #print content
        self.assert_(content == in_text)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
