import sys
import Node as N
import ProcessData as P


def uniform_cost_search(prepared_data, src, dest):
    # Creating closed set
    closed = []

    # Creating fringe
    fringe = []

    # Tracking number of nodes expanded
    nodes_expanded = 0

    # Tracking number of nodes generated
    nodes_generated = 1

    # Inserting initial node into the fringe
    fringe.append(N.Node(src, None, 0, 0))

    while len(fringe) > 0:
        # Dequeue a node from the fringe
        current_node = fringe.pop(0)
        # Incrementing node expansion counter
        nodes_expanded += 1

        # Check if the front node in the queue is the goal
        if current_node.state == dest:
            # The cost of current node will be the distance
            distance = current_node.cost
            # To keep track of the steps taken to get to this node
            steps_list = []

            # While the current_node exists we can then trace back the path from which it was reached
            while current_node:
                # Extracting the parent node from the current_node
                current_node_parent = current_node.parent
                if current_node.parent:
                    # Check if any states have current node as the destination
                    # If yes, we can get the distance from that node to the current node and then append to steps list
                    for a in prepared_data[current_node_parent.state]:
                        if a[0] == current_node.state:
                            steps_list.append(
                                current_node_parent.state + ' to ' + current_node.state + ', ' + str(a[1]) + ' km')
                current_node = current_node_parent

            print('nodes expanded: ' + str(nodes_expanded))
            print('nodes generated: ' + str(nodes_generated))
            print('distance: ' + str(distance) + ' km')
            print('route:')
            # Printing the route
            print('\n'.join(x for x in steps_list[::-1]))
            # Stop the loop, reached goal
            sys.exit()
        else:
            # If the current node is not in the closed then we add it to the closed list and generate successors
            if current_node.state not in closed:
                closed.append(current_node.state)
                successor_list = []

                for d in prepared_data[current_node.state]:
                    # We add the cost of current node to the next node
                    cost = current_node.cost + d[1]
                    # Adding g(n) as this is uninformed search and adding the node to successor list
                    successor_list.append(N.Node(d[0], current_node, cost, 0))
                # Appending the successors to the fringe and increment the node generated counter
                for successor in successor_list:
                    fringe.append(successor)
                    nodes_generated += 1

                # Sorting the fringe w.r.t g(n) as this is uninformed search
                fringe = sorted(fringe, key=lambda x: x.cost)

    # This code gets executed if the destination node is unreachable
    print('nodes expanded: ' + str(nodes_expanded))
    print('nodes generated: ' + str(nodes_generated))
    print('distance: infinity')
    print('route:\nnone')


def a_star_search(prepared_data, src, dest, heuristic_data):
    # Creating closed set
    closed = []

    # Creating fringe
    fringe = []

    # Tracking number of nodes expanded
    nodes_expanded = 0

    # Tracking number of nodes generated
    nodes_generated = 1

    # Inserting initial node into the fringe
    fringe.append(N.Node(src, None, 0, heuristic_data[src]))

    while len(fringe) > 0:
        # Dequeue a node from the fringe
        current_node = fringe.pop(0)
        # Incrementing node expansion counter
        nodes_expanded += 1

        # Check if the front node in the queue is the goal
        if current_node.state == dest:
            # The cost of current node will be the distance
            distance = current_node.cost
            # To keep track of the steps taken to get to this node
            steps_list = []

            # While the current_node exists we can then trace back the path from which it was reached
            while current_node:
                # Extracting the parent node from the current_node
                current_node_parent = current_node.parent
                if current_node.parent:
                    # Check if any states have current node as the destination
                    # If yes, we can get the distance from that node to the current node and then append to steps list
                    for a in prepared_data[current_node_parent.state]:
                        if a[0] == current_node.state:
                            steps_list.append(
                                current_node_parent.state + ' to ' + current_node.state + ', ' + str(a[1]) + ' km')
                current_node = current_node_parent

            print('nodes expanded: ' + str(nodes_expanded))
            print('nodes generated: ' + str(nodes_generated))
            print('distance: ' + str(distance) + ' km')
            print('route:')
            # Printing the route
            print('\n'.join(x for x in steps_list[::-1]))
            # Stop the loop, reached goal
            sys.exit()
        else:
            # If the current node is not in the closed then we add it to the closed list and generate successors
            if current_node.state not in closed:
                closed.append(current_node.state)
                successor_list = []

                for d in prepared_data[current_node.state]:
                    # We add the cost of current node to the next node
                    cost = current_node.cost + d[1]
                    # Adding g(n) + h(n) as this is informed search and adding the node to successor list
                    successor_list.append(N.Node(d[0], current_node, cost, cost + heuristic_data[d[0]]))
                # Appending the successors to the fringe and increment the node generated counter
                for successor in successor_list:
                    fringe.append(successor)
                    nodes_generated += 1

                # Sorting the fringe w.r.t f(n) as this is uninformed search
                fringe = sorted(fringe, key=lambda x: x.heuristic_cost)

    # This code gets executed if the destination node is unreachable
    print('nodes expanded: ' + str(nodes_expanded))
    print('nodes generated: ' + str(nodes_generated))
    print('distance: infinity')
    print('route:\nnone')


def main():
    args = len(sys.argv)

    input_file = sys.argv[1]
    src = sys.argv[2]
    dest = sys.argv[3]

    with open(input_file, 'r') as file:
        data = file.read().split('\n')

    prepared_data = P.prepareData(data)

    if args == 4:
        uniform_cost_search(prepared_data, src, dest)
    elif args == 5:
        heuristic_file = sys.argv[4]
        with open(heuristic_file, 'r') as file:
            data = file.read().split('\n')
        heuristic_data = P.prepareHeuristicData(data)
        a_star_search(prepared_data, src, dest, heuristic_data)
    else:
        print('Invalid number of arguments...')
        sys.exit()


if __name__ == '__main__':
    main()
