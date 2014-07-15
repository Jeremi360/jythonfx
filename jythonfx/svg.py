from javafx.scene import Group
from javafx.scene import shape
from xml.dom import minidom
import os

class SVGLoader(Group):
    def __init__(self, svg_file):
        doc = minidom.parse(svg_file)  # parseString also exists
        self.doc = doc.getElementsByTagName("svg")[0]
        doc.unlink()
        print self.doc
        self._set_layers()
        

    def _set_layers(self):
        layers = self.doc.getElementsByTagName('g')
        print layers
        ids = [layer.getAttribute('g') for layer
                        in self.doc.getElementsByTagName('id')]

        for d, l in ids, layers:
            Layer = Group()
            self._set_paths(Layer, l, d)
            self.getChildren().add(Layer)
            setattr(self, id, Layer)
            print "self." + d


    def _set_paths(self, fxlayer, svglayer, prefix = ""):
        paths = [path.getAttribute('d') for path
                        in svglayer.getElementsByTagName('path')]
        ids = [path.getAttribute('id') for path
                        in svglayer.getElementsByTagName('path')]

        for d, p in ids, paths:
            Path = shape.SVGPath()
            Path.setContent(p)
            setattr(self,  prefix + d, Path)
            fxlayer.getChildren().add(Path)
            print "self." + prefix + d



svgF =  os.path.join('..', 'samples', 'Test.svg')
svgO = SVGLoader(svgF)



