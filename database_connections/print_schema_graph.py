#%%

from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from eralchemy import render_er
import pydot


graph = create_schema_graph(metadata=MetaData('sqlite:///test.db'),
                            # The image could get very big showing the datatypes
                            show_datatypes=False,
                            # ditto for indexes
                            show_indexes=False,
                            # From left to right (instead of top to bottom)
                            rankdir='LR',
                            # Don't try to join the relation lines together
                            concentrate=False
                            )

graph.write_png('my_erd.png')

engine = create_engine('sqlite:///test.db')
print(engine.table_names())

metadata = MetaData('sqlite:///test.db')
print(metadata)

file = 'testdb.jpg'
render_er(metadata, file)

print(pydot.find_graphviz())
