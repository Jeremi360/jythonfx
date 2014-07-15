from javafx.scene import Group
from javafx.scene import shape
from xml.dom import minidom
import os

class SVGLoader(Group):
    def __init__(self, svg_file):
        self.doc = minidom.parse(svg_file)  # parseString also exists
        test = self._set_paths()
        self.doc.unlink()
        #print test

    def _set_paths(self, prefix = ""):
        paths = [path.getAttribute('d') for path
                        in self.doc.getElementsByTagName('path')]
        ids = [path.getAttribute('id') for path
                        in self.doc.getElementsByTagName('path')]

        for d, p in ids, paths:
            Path = shape.SVGPath(p)
            setattr(self,  prefix + d, Path)
            print "self." + prefix + d



svgF =  os.path.join('..', 'samples', 'Test.svg')
svgO = SVGLoader(svgF)



