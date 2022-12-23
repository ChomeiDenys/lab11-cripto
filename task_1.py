import math

# Function to check the point


def checkpoint( x):

	# checking the equation of
	# ellipse with the given point
	p = ((math.pow((x), 3)+ x + 1) % 23)

	return p


# Driver code
if __name__ == "__main__":

	x = 2


	if (checkpoint(x)> 1):
		print("Outside")

	elif (checkpoint( x) == 1):
		print("On the ellipse")

	else:
		print("Inside")


