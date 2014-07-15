from javafx.scene import Group
from xml.dom import minidom
import os

class SVGLoader(Group):
    def __init__(self, svg_file):
        self.doc = minidom.parse(svg_file)  # parseString also exists

        self.doc.unlink()
        print paths
        print ids

    def _set_paths(self):
        paths = [path.getAttribute('d') for path
                        in self.doc.getElementsByTagName('path')]
        ids = [path.getAttribute('id') for path
                        in self.doc.getElementsByTagName('path')]

        return {ids:paths}



svgF =  os.path.join('..', 'samples', 'Test.svg')
svgO = SVGLoader(svgF)



