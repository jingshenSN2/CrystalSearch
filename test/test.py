import time

from src import CrystalParser, MatchRater, GraphHandler

cell = CrystalParser.parse_res('test/c21_origin.res')
cell.calc_neighbors()
graph = GraphHandler.graph_converter(cell)
target = GraphHandler.max_subgraph(graph)
# GraphHandler.draw_graph(target, direction='a')
# GraphHandler.draw_graph(target, direction='b')
GraphHandler.draw_graph(target, direction='c')

pattern = CrystalParser.parse_pdb('test/query.pdb')
pattern.calc_neighbors()
graph2 = GraphHandler.graph_converter(pattern)
query = GraphHandler.max_subgraph(graph2)
# GraphHandler.draw_graph(query, direction='a')
# GraphHandler.draw_graph(query, direction='b')
GraphHandler.draw_graph(query, direction='c')


start = time.process_time()
result1 = MatchRater.match_1(target, query, 10)
if result1:
    for i in result1:
        GraphHandler.draw_graph_highlight(target, i)
        rmsd = MatchRater.rmsd(i)
        print('rmsd %.2f' % rmsd)
        break
end = time.process_time()
print(end - start)

start = time.process_time()
result2 = MatchRater.match_2(target, query, 5)
if result2:
    for i in result2:
        GraphHandler.draw_graph_highlight(target, i)
        rmsd = MatchRater.rmsd(i)
        print('rmsd %.2f' % rmsd)
        break
end = time.process_time()
print(end - start)