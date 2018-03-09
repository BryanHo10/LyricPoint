#The purpose of this application is to automatically import lyrics from an online source onto
# a created .pptx file
from bs4 import BeautifulSoup as soup
import bs4
import urllib.request
import requests
from pptx import Presentation
from pptx.shapes import *
import datetime
from pptx.util import *
from pptx.enum.text import *
#datetime.date.today()

class SlideShow:

	def __init__(self,title,artist):
		self._title=title
		self._artist=artist
		self._base='https://www.musixmatch.com'
		self._filename='Worship {}'.format(datetime.date.today().strftime('%m-%d'))
		self.headers = 	{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
		self.grabSongData()

	def grabSongData(self):
		base_url='https://www.musixmatch.com/search/'
		songTitle=self._title.split(' ')
		songArtist=self._artist.split(' ')
		my_url=''
		songInfo=songTitle+songArtist

		for i in range(len(songInfo)-1):
			base_url+=songInfo[i]+'%20'

		my_url+=base_url+songInfo[-1]

		htmlPage= requests.get(my_url,headers=self.headers)
		htmlPage.raise_for_status()
		page_soup=soup(htmlPage.text,"html.parser")

		songUrl=page_soup.findAll("h2",{'class':'media-card-title'})[0]
		songUrl=songUrl.find('a',{'class':'title'})['href']
		my_url=self._base+songUrl

		htmlPage= requests.get(my_url,headers=self.headers)
		htmlPage.raise_for_status()
		page_soup=soup(htmlPage.text,"html.parser")

		songLyrics=page_soup.findAll('p',{'class':'mxm-lyrics__content'})
		songLyrics[0]=songLyrics[0].text
		songLyrics[1]=songLyrics[1].text
		self.splitLyrics(songLyrics)

	def splitLyrics(self,lyrics):
		refinedLyric=[]
		for verse in lyrics:
			refinedLyric+=(verse.split('\n\n'))
		print(refinedLyric)
		self._lyrics=refinedLyric
		self.makeSlide()


	def makeSlide(self):
		prs=Presentation()

		blank_slide_layout = prs.slide_layouts[5]
		for verse in self._lyrics:
			slide = prs.slides.add_slide(blank_slide_layout)
			shapes = slide.shapes
			left = top = width = height = Inches(1)
			txBox = slide.shapes.add_textbox(left+Inches(3.5), top+Inches(0.25), width, height)
			tf = txBox.text_frame

			title = slide.shapes.title
			title.text = self._title
			p = tf.add_paragraph()
			p.text = verse
			p.font.size = Pt(32)
			p.alignment = PP_ALIGN.CENTER

		prs.save(self._filename+'.pptx')


'''
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Hello, World!"
subtitle.text = "python-pptx was here!"

prs.save('test.pptx')'''





'''
prs = Presentation()
bullet_slide_layout = prs.slide_layouts[1]

slide = prs.slides.add_slide(bullet_slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = 'Adding a Bullet Slide'

tf = body_shape.text_frame
tf.text = 'Find the bullet slide layout'

p = tf.add_paragraph()
p.text = 'Use _TextFrame.text for first bullet'
p.level = 1

p = tf.add_paragraph()
p.text = 'Use _TextFrame.add_paragraph() for subsequent bullets'
p.level = 2

prs.save('test.pptx')'''





'''
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

left = top = width = height = Inches(1)
txBox = slide.shapes.add_textbox(left, top, width, height)
tf = txBox.text_frame

tf.text = "This is text inside a textbox"

p = tf.add_paragraph()
p.text = "This is a second paragraph that's bold"
p.font.bold = True

p = tf.add_paragraph()
p.text = "This is a third paragraph that's big"
p.font.size = Pt(40)

prs.save('test.pptx')'''