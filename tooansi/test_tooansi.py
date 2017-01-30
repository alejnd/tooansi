
#Use green command to run a nicer test output from test directory
#from PIL import Image
import unittest
import run
from io import FileIO
from PIL import Image, ImageDraw
import os 

class ServerTests(unittest.TestCase):

    def setUp(self):
        self.app = run.app.test_client()
        if not os.path.exists('/tmp/tooansitests'): os.mkdir('/tmp/tooansitests')

    def tearDown(self):
        pass

    def testIsUp(self):
        rv = self.app.get('/upload')
        assert rv.status_code == 405

    def testIsaFile(self):
        rv = self.app.post('/upload',data=dict(file=''))
        assert b'Error: No file given' in rv.data

    def testValidFormat(self):
        #gif image for testing
        self.giffile = '/tmp/tooansitests/testgif.gif'
        gifimg  = Image.new('RGBA',(100, 100))
        draw    = ImageDraw.Draw(gifimg)
        draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))
        gifimg.save(self.giffile, 'GIF', transparency=0)

        rv = self.app.post('/upload',data=dict(file=FileIO(self.giffile)))
        os.remove(self.giffile)
        assert b'Error: file must be PNG image' in rv.data

    def testPNGFile(self):
        #png image for testing
        pngfile = '/tmp/tooansitests/testpng.png'
        pngimg  = Image.new('RGB',(100, 100),(255,0,0))
        draw    = ImageDraw.Draw(pngimg)
        draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))
        pngimg.save(pngfile, 'PNG')

        rv = self.app.post('/upload', data=dict(file=FileIO(pngfile)))
        #os.remove(pngfile) #wierd stuff... not today
        assert rv.status_code == 200

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(ServerTests)
    unittest.TextTestRunner(verbosity=2).run(suite)