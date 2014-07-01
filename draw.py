

from pytagcloud import create_tag_image


def drawGraph(WordSelected, PictureFilename):
	create_tag_image(WordSelected, 'cloud.png', size=(900, 600), fontname='simhei')
	return None
	