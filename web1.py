import streamlit as st
import funct1


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    funct1.write_todos(todos)



todos = funct1.get_todos()

st.title("My Todo App")
st.subheader("This is my todo App.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        funct1.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")