SIZE = 500
r = g = b = 0

img = "P3 " + str(SIZE) + " " + str(SIZE) + " 255 "

for i in range( SIZE * SIZE ):
	x = (i % SIZE)
	y = (i / SIZE)
	if ( (x**2) + (y**2) <= SIZE * SIZE):
		r = ( r + 3 ) % 255
		b = ( b + 3 ) % 255
		g = ( b + 3 ) % 255
	else:
		r = 0 
		g = 113 
		b = 113
	img += "%d %d %d " %(r, g, b)

f = open("pic.ppm", "w")
f.write(img)
f.close()
