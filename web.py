import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+'\n')
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()

st.text_input(label="Enter a to-do", placeholder="Add new to-do...", on_change=add_todo, key="new_todo")
