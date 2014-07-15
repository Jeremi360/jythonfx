from javafx.scene import Group
from xml.dom import minidom
import os

class SVGLoader(Group):
    def __init__(self, svg_file):
        doc = minidom.parse(svg_file)  # parseString also exists
        paths = [path.getAttribute('d') for path
                        in doc.getElementsByTagName('path')]
        ids = [path.getAttribute('id') for path
                        in doc.getElementsByTagName('path')]
        doc.unlink()
        print paths, ids

svgF =  os.path.join('..', 'samples', 'Test.svg')
svgO = SVGLoader(svgF)



