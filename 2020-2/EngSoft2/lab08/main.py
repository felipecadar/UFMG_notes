import os, re
import networkx as nx

if __name__ == "__main__":

    # file_counter = 0
    # node_file = {}
    G = nx.Graph()

    pattern = re.compile("[a-z0-9]{40}")
    count = 0

    files_now = []
    with open("log.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            m = pattern.match(line)
            if m:
                for i in range(len(files_now)):
                    if not (files_now[i] in list(G.nodes)):
                        G.add_node(files_now[i])

                    for j in range(i+1, len(files_now)):
                        if not (files_now[j] in list(G.nodes)):
                            G.add_node(files_now[j])

                        if not G.has_edge(files_now[i], files_now[j]):
                            G.add_edge(files_now[i], files_now[j], weight=0)

                        G[files_now[i]][files_now[j]]["weight"] += 1

                files_now = []
                count += 1
            else:
                # print(line.strip())
                files_now.append(line.strip())

    print("\nTop pair changes")
    soreted_edges = sorted(list(G.edges), key=lambda e: G[e[0]][e[1]]['weight'], reverse=True)
    for n in range(10):
        i, j = soreted_edges[n]
        print("{:>20} -> {:>20}: {}".format(i, j,  G[i][j]['weight'] ))

    print("\nTop Conections")
    soreted_edges = sorted(list(G.nodes), key=lambda n: G.degree(n), reverse=True)
    for n in range(10):
        i = soreted_edges[n]
        # print(len)
        print("{:>25} : {}".format(i, G.degree(i) ))

    print("\nTop Conections + Weight")
    soreted_edges = sorted(list(G.nodes), key=lambda n: G.degree(n), reverse=True)
    for n in range(10):
        i = soreted_edges[n]
        # print(len)
        print("{:>25} : {}".format(i, G.degree(i, weight="weight") ))


    print("Total Commits:", count)