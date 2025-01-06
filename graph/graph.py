import uuid

from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from agents import ocr_agent
from state.graph_state import GraphState

global graph

def create_graph():
    global graph
    workflow = StateGraph(state_schema=GraphState)
    workflow.add_node("entry_point", lambda x: x)
    workflow.add_edge(START, "entry_point")
    workflow.add_node("clean", ocr_agent.run)
    workflow.add_edge("entry_point", "clean")
    workflow.add_edge("clean", END)
    memory = MemorySaver()
    graph = workflow.compile(checkpointer=memory)
    return graph

# Function to invoke the compiled graph externally
def invoke_graph(state, callables):
    # Ensure the callables parameter is a list as you can have multiple callbacks
    if not isinstance(callables, list):
        raise TypeError("callables must be a list")
    # Invoke the graph with the current messages and callback configuration
    return graph.invoke(state, config={"callbacks": callables, "configurable":{"thread_id": uuid.uuid4()}})
