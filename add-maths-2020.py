from manim import *

edges = [
    (0, 1),
    (0, 2),
    (0, 5),
    (1, 3),
    (1, 2),
    (2, 4),
    (3, 6),
    (3, 4),
    (4, 6),
    (4, 5),
    (5, 6)
]

# list of pairs
tree_diagram_list = []


def main():
    # list of list
    adj = [[1, 2, 5], [3, 2, 0], [1, 4, 0], [6, 4, 1], [3, 6, 5, 2], [4, 6, 0], [5, 4, 3]]

    def threeGivenAB():
        # list of list
        trails = []

        def find_all_trails(now, visited_edges, visited_nodes):
            visited_nodes.append(now)
            if now == 6:
                trails.append(visited_nodes)
                return
            for nxt in adj[now]:
                edge = [nxt, now]
                if edge[0] > edge[1]:
                    edge[0], edge[1] = edge[1], edge[0]
                if edge in visited_edges:
                    continue
                nxt_visited_edges = visited_edges.copy()
                nxt_visited_edges.append(edge)
                find_all_trails(nxt, nxt_visited_edges.copy(), visited_nodes.copy())

        find_all_trails(0, [], [])
        print("Number of trails from A to B: " + str(len(trails)))
        print("Number of legal trails from A to B: " + str(len([x for x in trails if len(x) <= 4])))
        for trail in trails:
            print(trail)

    threeGivenAB()

    def ABGivenThree():
        # list of list
        trails = []

        def find_all_trails(now, visited_edges, visited_nodes):
            visited_nodes.append(now)
            if 3 >= len(visited_edges) > 0:
                trails.append(visited_nodes)
                if len(visited_edges) == 3:
                    return
            for nxt in adj[now]:
                edge = [nxt, now]
                if edge[0] > edge[1]:
                    edge[0], edge[1] = edge[1], edge[0]
                if edge in visited_edges:
                    continue
                nxt_visited_edges = visited_edges.copy()
                nxt_visited_edges.append(edge)
                tree_diagram_list.append((now, nxt))
                find_all_trails(nxt, nxt_visited_edges.copy(), visited_nodes.copy())

        find_all_trails(0, [], [])
        print("Number of trails at most 3: " + str(len(trails)))
        print("Number of trails from A to B: " + str(len([x for x in trails if x[-1] == 6])))
        for trail in trails:
            print(trail)

    ABGivenThree()


class MovingVertices(Scene):
    def construct(self):
        vertices = []
        for i in range(0, 7):
            vertices.append(i)
        g = Graph(vertices, edges, vertex_config={
            0: {"fill_color": RED},
            6: {"fill_color": RED}
        })
        self.play(ShowCreation(g))
        self.wait()
        self.play(
            g[0].animate.move_to([-4, 0, 0]),
            g[1].animate.move_to([-2, 2, 0]),
            g[2].animate.move_to([-2, 0, 0]),
            g[3].animate.move_to([0, 2, 0]),
            g[4].animate.move_to([0, 0, 0]),
            g[5].animate.move_to([0, -2, 0]),
            g[6].animate.move_to([2, 0, 0]),
        )
        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)
        self.play(
            Write(A),
            Write(B)
        )
        new_edge = g.edges[(1, 3)].copy()
        new_edge.set_color(RED)
        self.play(Transform(g.edges[(1, 3)], new_edge))
        line = g.edges[(0, 1)].copy().set_color(RED)
        self.play(ShowCreation(line, run_time=2))
        self.wait()


main()
print(tree_diagram_list)


class TreeDiagram(Scene):
    CONFIG = {
        "y_max": 50,
        "y_min": -50,
        "x_max": 50,
        "x_min": -50,
    }

    # Setup the scenes
    def setup(self):
        Scene.setup(self)

    def construct(self):
        cols = [
            [Text(x) for x in ['0']],
            [Text(x) for x in ['1', '2', '5']],
            [Text(x) for x in ['3', '2', '1', '4', '4', '6']],
        ]

        start = [0, 2, 2.5]
        dy = [0, 2, 1]

        for coldex, col in enumerate(cols):
            for itemdex, item in enumerate(col):
                item.move_to([coldex, start[coldex] - dy[coldex] * itemdex, 0])
                self.play(Write(item))
