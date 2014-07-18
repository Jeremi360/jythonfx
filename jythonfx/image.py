# -*- coding: utf-8 *-*
import fix
fix.getJavaFX()

from java.io import File
from javafx.scene.image import Image, ImageView as IV

class Image(IV):
    def __init__(self, path_to_img):
        f = File(path_to_img).toURI().toString()
        img = Image(f)
        super(Image, self).__init__(img)
