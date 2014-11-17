#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="  Up  ", background= "white")
		self.up.grid(row=0,column=2)
					
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "white")
		self.down.grid(row=2,column=2)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "white")
		self.left.grid(row=1,column=1)	
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "white")
		self.right.grid(row=1,column=3)				
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                self.down.bind("<Button-1>", self.moveDown)
		self.left.bind("<Button-1>", self.moveLeft)
		self.right.bind("<Button-1>", self.moveRight) 
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

	def moveUp(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,-10) 
                
        def moveDown(self, event):   
		global player
		global drawpad
                drawpad.move(player,0,10)
                
        def moveLeft(self, event):   
		global player
		global drawpad
		global drawpadwidth
                global drawpadheight
                x1, y1, x2 , y2 = drawpad.coords(player)
                if x1 > 0:
                     drawpad.move(player,-10,0)
                
        def moveRight(self, event):   
		global player
		global drawpad
		global drawpadwidth
                global drawpadheight
                x1, y1, x2 , y2 = drawpad.coords(player)
                if x2 < 480:
                     drawpad.move(player,10,0)                       
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global target
	    global direction
	    drawpad.move(target,0,direction)
	    drawpad.move(target,direction,0)
	    
	    # Insert the code here to make the target move, bouncing on the edges    
	        
	        
            
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                x1,y1,x2,y2 = drawpad.coords(player)
	        targetx1, targety1, targetx2, targety2 = drawpad.coords(target)
	        if (targetx1 < x1 and targetx2 > x2 and targety1 < y1 and targety2 > y2):
                    drawpad.itemconfig(target,fill='red')
                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)
root.mainloop()