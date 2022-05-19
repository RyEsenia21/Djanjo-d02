from elem import Elem, Text

class Html(Elem):
	def __init__(self, content=None, attr={}, tag='html',  tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Head(Elem):
	def __init__(self, content=None, attr={}, tag='head',  tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Body(Elem):
	def __init__(self, content=None, attr={}, tag='body',  tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Title(Elem):
	def __init__(self, content=None, attr={}, tag='title', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Meta(Elem):
	def __init__(self, content=None, attr={}, tag='meta', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Img(Elem):
	def __init__(self, content=None, attr={}, tag='img', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Table(Elem):
	def __init__(self, content=None, attr={}, tag='table', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Th(Elem):
	def __init__(self, content=None, attr={}, tag='th', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Tr(Elem):
	def __init__(self, content=None, attr={}, tag='tr', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Td(Elem):
	def __init__(self, content=None, attr={}, tag='td', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Ul(Elem):
	def __init__(self, content=None, attr={}, tag='ul',  tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Ol(Elem):
	def __init__(self, content=None, attr={}, tag='ol', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Li(Elem):
	def __init__(self, content=None, attr={}, tag='li', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class H1(Elem):
	def __init__(self, content=None, attr={}, tag='h1', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class H2(Elem):
	def __init__(self, content=None, attr={}, tag='h2', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class P(Elem):
	def __init__(self, content=None, attr={}, tag='p', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Div(Elem):
	def __init__(self, content=None, attr={}, tag='div',  tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Span(Elem):
	def __init__(self, content=None, attr={}, tag='span', tag_type='double'):
		super().__init__(tag, attr, content, tag_type)

class Hr(Elem):
	def __init__(self, content=None, attr={}, tag='hr', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

class Br(Elem):
	def __init__(self, content=None, attr={}, tag='br', tag_type='simple'):
		super().__init__(tag, attr, content, tag_type)

def main():
    page = Html([Head(Title('"Hello ground!"')), Body([H1('"Oh no, not again!"'), Img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})])])
    print(page)

if __name__ == '__main__':
	main()