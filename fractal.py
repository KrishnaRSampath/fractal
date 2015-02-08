# fractal.py
import turtle

def fractal_tree(trunk_length):
	window = turtle.Screen()
	window.bgcolor("black")

	t = turtle.Turtle()
	t.color("yellow")
	t.speed(3)

	t.left(90)
	t.forward(trunk_length)

	depth = 3
	left_fork(t, trunk_length, depth)
	t.backward(trunk_length)
	right_fork(t, trunk_length, depth-1 )
	left_fork(t, trunk_length, depth-2)
	t.backward(trunk_length)
	right_fork(t, trunk_length, depth-2 )
	left_fork(t, trunk_length, depth-3)


 	window.exitonclick()




def left_fork(turtle, branch_length, depth):
 	if depth == 0:
 		turtle.backward(branch_length)
 		right_fork(turtle,branch_length, depth+1)
 		return

	turtle.left(25)
	turtle.forward(branch_length)
	left_fork(turtle, branch_length, depth-1)


def right_fork(turtle, branch_length, depth):
	if depth == 0:
 		turtle.backward(branch_length)
 		return
	turtle.right(25)
	turtle.forward(branch_length)
	right_fork(turtle, branch_length, depth-1)
	



fractal_tree(50)

