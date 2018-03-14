from slide import *

title=input("Enter the song title: ")
artist=input("Enter the song artist: ")

lyricSlide=SlideShow(title,artist)
choice=input("Would you like to import lyrics to slides (Y/N): ")
if(choice.lower()=='y'):
	check=input("Are you sure? Press 1 to confirm: ")
	if(check=='1'):
		lyricSlide.makeSlide()
else:
	lyricSlide.displayLyrics()

choice=input('Would you like to add another song?(y/n): ')
while(choice.lower()=='y'):
	title=input("Enter the song title: ")
	artist=input("Enter the song artist: ")
	check=input("Are you sure? Press 1 to confirm: ")
	if(check=='1'):
		lyricSlide.addSong(title,artist)
	else:
		continue
	choice=input('Would you like to add another song?(y/n): ')
