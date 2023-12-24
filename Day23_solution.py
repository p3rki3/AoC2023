import AoCFramework as AoC
import networkx as nx
from networkx.classes.function import path_weight

def part_1():
    for row, line in enumerate(Lines):
        for col, ch in enumerate(line):
            pt = (row, col)
            if ch == "#":
                Grid1.remove_node(pt)
                Grid2.remove_node(pt)
            elif dp := {">": (0, -1), "<": (0, 1), "^": (1, 0), "v": (-1, 0)}.get(ch):
                Grid1.remove_edge(pt, (row + dp[0], col + dp[1]))
    return (max(map(len, nx.all_simple_edge_paths(Grid1, startpt, endpt))))

def part_2():
    nodes = [node for node in Grid2.nodes if len(Grid2.edges(node)) == 2]
    for node in nodes:
        vert1, vert2 = list(Grid2.neighbors(node))
        Grid2.add_edge(vert1, vert2, d = sum(Grid2.edges[node, vert].get("d", 1) for vert in (vert1, vert2)))
        Grid2.remove_node(node)
    return (max(path_weight(Grid2, path, "d") for path in nx.all_simple_paths(Grid2, startpt, endpt)))

Lines, Rows = AoC.Init("data/day23.txt", test=False)
Cols, startpt, endpt = len(Lines[0]), (0, Lines[0].index(".")), (Rows - 1, Lines[-1].index("."))
Grid1, Grid2 = nx.grid_2d_graph(Rows, Cols, create_using=nx.DiGraph), nx.grid_2d_graph(Rows, Cols)
AoC.verify(2394, 6554)
AoC.run(part_1, part_2)
