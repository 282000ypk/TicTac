from graphics import *
import sys as sys

""" index for a win situation """
win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
data={}
window=GraphWin("Tic Tac",500,500)
window.setCoords(0,0,500,500)
boxx=[]
flag=True
class moves:
	def __init__(self):
		self.count=0

def restart():
	boxx.clear()
	for obj in window.items[:]:
		obj.undraw()
	window.update()
	block=Rectangle(Point(50,460),Point(450,490))
	block.setFill(color_rgb(200,50,0))
	block.draw(window)
	exit=Text(Point(250,475),"EXIT")
	exit.setStyle("bold")
	exit.draw(window)

	moves.count=0
	global data
	data={1:"z",2:"z",3:"z",4:"z",5:"z",6:"z",7:"z",8:"z",9:"z"}
	global flag
	flag=True
	window.setBackground("grey")
	box=Rectangle(Point(50,50),Point(450,450));
	box.setWidth(3)
	box.setFill("grey")	
	box.draw(window)
	x=[Rectangle(Point(50,320),Point(180,450)),1]
	boxx.append(x)
	x=[Rectangle(Point(180,320),Point(320,450)),2]
	boxx.append(x)
	x=[Rectangle(Point(320,320),Point(450,450)),3]
	boxx.append(x)
	x=[Rectangle(Point(50,180),Point(180,320)),4]
	boxx.append(x)
	x=[Rectangle(Point(180,180),Point(320,320)),5]
	boxx.append(x)
	x=[Rectangle(Point(320,180),Point(450,320)),6]
	boxx.append(x)
	x=[Rectangle(Point(50,50),Point(180,180)),7]
	boxx.append(x)
	x=[Rectangle(Point(180,50),Point(320,180)),8]
	boxx.append(x)
	x=[Rectangle(Point(320,50),Point(450,180)),9]
	boxx.append(x)

	for i in boxx:
		i[0].setWidth(3)
		i[0].draw(window)


def check():
	for i in win:
		if(data[i[0]]=="x" and data[i[1]]=="x" and data[i[2]]=="x"):
			return True;

		if(data[i[0]]=="o" and data[i[1]]=="o" and data[i[2]]=="o"):
			return True;

def play():
	global flag
	if(check()):
		if(moves.count%2!=0):
			window.setBackground("green")
			msg=Text(Point(250,20),"O win's\nClick to play again")
			msg.draw(window)
		else:
			window.setBackground("red")
			msg=Text(Point(250,20),"X win's\nClick to play again")
			msg.draw(window)
		window.getMouse()
		restart()
		play()
	elif moves.count==9:
		msg=Text(Point(250,20),"Draw\nClick to play again")
		msg.draw(window)
		window.getMouse()
		restart()
		play()
	else:
		click=window.getMouse()
		if(click.getX()>50 and click.getY()>450 and click.getX()<450 and click.getY()<500):
			sys.exit()
		if(click.getX()>50 and click.getY()>50 and click.getX()<450 and click.getY()<450):
			for b in boxx:
				p1=b[0].getP1()
				p2=b[0].getP2()
				if(p2.getX()>=click.getX() and p1.getX()<=click.getX() and p2.getY()>=click.getY() and p1.getY()<=click.getY()):
					boxx.remove(b)
					if(moves.count%2!=0):
						x=Text(b[0].getCenter(),"X")
						x.setStyle("bold")
						x.setSize(30)
						x.draw(window)
						#b[0].setFill("red")
						data[b[1]]="x"
					else:
						x=Text(b[0].getCenter(),"O")
						x.setStyle("bold")
						x.setSize(30)
						x.draw(window)
						#b[0].setFill("green")
						data[b[1]]="o"
					moves.count+=1
					break
			play()
		else:
			play()

restart() 
play()
click=window.getMouse()

