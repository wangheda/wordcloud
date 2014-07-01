

from pytagcloud import create_tag_image, make_tags


def drawGraph(WordSelected, PictureFilename):
	tags = make_tags(WordSelected, minsize=18, maxsize=120)
	create_tag_image(tags, PictureFilename, size=(900, 600), fontname='SimHei')
	return None
	