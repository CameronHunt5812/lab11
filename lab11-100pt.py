##########################################
#                                        #
#           100pt - Lab 11               # 
#                                        #
##########################################

# Make the ball "wrap" instead of bouncing - when it hits the right
# edge of the window, it should reappear at the left side and continue moving
# to the right. 

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

# Create the oval
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
direction = 1
# Create our animation function
def animate():
    
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    # Moove the cercle to the left side of the skreen
    if x2 > drawpad.winfo_width():
        drawpad.move(circle, -(drawpad.winfo_width()) + (x2 - x1),0)
    #Move our oval object by the value of direction
    drawpad.move(circle,1,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()
