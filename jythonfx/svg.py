from javafx.scene import Group
from javafx.scene import shape
from xml.dom import minidom
import os

class SVGLoader(Group):
    def __init__(self, svg_file):
        self.doc = minidom.parse(svg_file)  # parseString also exists
        self._set_layers()
        self.doc.unlink()

    def _set_layers(self, prefix = ""):
        layers = self.doc.getElementsByTagName('g')
        print layers
        ids = [layer.getAttribute('g') for layer
                        in self.doc.getElementsByTagName('id')]

    def _set_paths(self, layer, prefix = ""):
        paths = [path.getAttribute('d') for path
                        in self.doc.getElementsByTagName('path')]
        ids = [path.getAttribute('id') for path
                        in self.doc.getElementsByTagName('path')]

        for d, p in ids, paths:
            Path = shape.SVGPath()
            Path.setContent(p)
            setattr(self,  prefix + d, Path)
            self.getChildren().add(Path)
            print "self." + prefix + d



svgF =  os.path.join('..', 'samples', 'Test.svg')
svgO = SVGLoader(svgF)



