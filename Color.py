class Color:
	black = (  0,  0,  0)
	gray  = (128,128,128) 
	white = (255,255,255)
	red   = (255,  0,  0)
	green = (  0,255,  0)
	blue  = (  0,  0,255)
	yellow  = (  255,  255,0,128)
	orange=(255,165,0)
	purple=(255,153,255)
	aqua=(0,255,255)
	lightGray = (200,200,200)
	darkGray = (90,90,90)
	teal = (0,137,123)
	pink = (255,64,129)
	lime =(198,255,0)
	brown = (141,110,99)

	def darken(c,amount):
		(r,g,b) = c
		if r > amount:
			r -= amount

		if g > amount:
			g -= amount
			
		if b > amount:
			b -= amount

		c = (r,g,b)

		return c
	