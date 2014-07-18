# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()

from java.io import File
from javafx.scene.image import ImageView as IV

class ImageView(IV):
    def __init__(self, path_to_img):
        f = File(path_to_img).toURI().toString()
        super(ImageView, self).__init__(f)
