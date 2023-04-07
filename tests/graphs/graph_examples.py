from course.data_structures import GraphEdge

########################################################
################# Graph as a Matrix ####################
########################################################

"""
          Graph                        Adjacency Matrix

           (10)                         0   1   2   3
      [0] ➜  ➜  ➜ [1]                 ----|---|---|---|
       ↑  ⬊  (5)   ↑                0 |  0  10   0   5
   (7) ↑     ⬊     ↑ (1)            1 |  0   0   0   0
       ↑   (2)   ⬊ ↑                2 |  7   0   0   0
      [2] ←  ←  ← [3]               3 |  0   1   2   0

    Legend: [] - node
            () - weight
            ➜  - direction
"""
graph_matrix_1 = [
    [0, 10, 0, 5],
    [0, 0, 0, 0],
    [7, 0, 0, 0],
    [0, 1, 2, 0],
]


# Graphs below are taken from: https://github.com/ThePrimeagen/kata-machine/blob/master/src/__tests__/graph.ts

"""

    >(1)<--->(4) ---->(5)
   /          |       /|
(0)     ------|------- |
   \   v      v        v
    >(2) --> (3) <----(6)

"""  # noqa: W605

graph_matrix_2 = [
    [0, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 5, 0, 2, 0],
    [0, 0, 18, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0],
]

########################################################
################## Graph as a List #####################
########################################################
"""
     > (1)<--->(4)<---->(5)
   </  ^       ^       /^
 (0)   | ------|------- |
   <\  v/      v        v
     > (2)<--->(3)<---->(6)
"""  # noqa: W605

graph_list_1 = [None] * 7

graph_list_1[0] = [
    GraphEdge(to=1, weight=3),
    GraphEdge(to=2, weight=1),
]

graph_list_1[1] = [
    GraphEdge(to=0, weight=3),
    GraphEdge(to=2, weight=4),
    GraphEdge(to=4, weight=1),
]
graph_list_1[2] = [
    GraphEdge(to=0, weight=1),
    GraphEdge(to=1, weight=4),
    GraphEdge(to=3, weight=7),
]
graph_list_1[3] = [
    GraphEdge(to=2, weight=7),
    GraphEdge(to=4, weight=5),
    GraphEdge(to=6, weight=1),
]
graph_list_1[4] = [
    GraphEdge(to=1, weight=1),
    GraphEdge(to=3, weight=5),
    GraphEdge(to=5, weight=2),
]
graph_list_1[5] = [
    GraphEdge(to=2, weight=18),
    GraphEdge(to=4, weight=2),
    GraphEdge(to=6, weight=1),
]
graph_list_1[6] = [
    GraphEdge(to=3, weight=1),
    GraphEdge(to=5, weight=1),
]

# -------------------------------------

graph_list_2 = [None] * 7
"""
     >(1)<--->(4) ---->(5)
    /          |       /|
 (0)    /------|------- |
    \   v      v        v
     >(2) --> (3) <----(6)
"""  # noqa: W605

graph_list_2[0] = [
    GraphEdge(to=1, weight=3),
    GraphEdge(to=2, weight=1),
]
graph_list_2[1] = [
    GraphEdge(to=4, weight=1),
]
graph_list_2[2] = [
    GraphEdge(to=3, weight=7),
]
graph_list_2[3] = []
graph_list_2[4] = [
    GraphEdge(to=1, weight=1),
    GraphEdge(to=3, weight=5),
    GraphEdge(to=5, weight=2),
]
graph_list_2[5] = [
    GraphEdge(to=2, weight=18),
    GraphEdge(to=6, weight=1),
]
graph_list_2[6] = [
    GraphEdge(to=3, weight=1),
]
