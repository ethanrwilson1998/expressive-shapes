# Expressive Shapes

A simple template app for the Expressive Shapes project built in Python using pyqt5.

To get started:

- Download this repo
> git clone [repo]
- Install pyqt5
> pip install pyqt5
- Replace the template code in *https://github.com/ethanrwilson1998/expressive-shapes/shapes.py*		

		def move(self, shapes):  
			# your movement code here, replace this sample code:  
			if self.x < 0:  
				self.direction = 1  
			if self.x + self.w >= canvas_width:  
				self.direction = -1  

			self.x += self.speed * self.direction  
			##########

- The template code moves rectangles horizontally and circles vertically, changing direction when they reach the edge of the canvas.  Triangles toggle directions to move in a square.
- When the move function is called, the list of all shapes in the scene is returned.  By using the information in this list, you will be able to plan a shape's movement based on the positions/colors/sizes of other shapes.

![Template in action](main-gif.gif)

# TODO:

- Accept parameters as args
- Create multiple test setups with different shape color size combinations
