SIZE = 100
r = g = b = 0

img = "P3 " + str(SIZE) + " " + str(SIZE) + " 255 "

for i in range( SIZE * SIZE ):
	x = (i % SIZE) % (SIZE / 3)
	y = (i / SIZE) % (SIZE / 3)
	if ( (x**2) + (y**2) <= SIZE ):
		r = 235 - x - y 
		b = 113 - x - y 
		g = 13
	else:
		r = 0 
		g += x * y
		b += (x + y)
	img += "%d %d %d " %(r, g, b)

f = open("pic.ppm", "w")
f.write(img)
f.close()
