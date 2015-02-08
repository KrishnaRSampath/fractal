# fractal.py
import turtle

def fractal_tree(trunk_length):
	window = turtle.Screen()
	window.bgcolor("black")

	tree = turtle.Turtle()
	tree.color("yellow")
	tree.speed(2)

	tree.left(90)
	tree.forward(trunk_length)

	max_depth = 3
	angle = 25
	total_nodes = 2**3
	nodes_done = 0

	# Call Recursive function "Tree-Builder"
	tree_builder(tree, max_depth, 0, trunk_length, angle, total_nodes, nodes_done)

	window.exitonclick()

def tree_builder(tree, max_depth, current_depth, branch_length, angle, total_nodes, nodes_done):

	#Done with whole tree when?
	if nodes_done == total_nodes:
		return

	if current_depth > max_depth:
		tree.circle(100)

	if current_depth == max_depth:
		nodes_done += 1
		tree.backward(branch_length)
		tree.right(angle*2)
		tree.forward(branch_length)
		nodes_done += 1
		tree.backward(branch_length)
		tree.left(angle)
		tree.backward(branch_length)
		tree.right(angle*3)
		current_depth -= 2

	tree.left(angle)
	tree.forward(branch_length)
	tree_builder(tree, max_depth, current_depth+1, branch_length, angle, total_nodes, nodes_done)



fractal_tree(50)

