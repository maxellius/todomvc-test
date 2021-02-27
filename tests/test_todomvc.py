from todomvc_tests.modul import todos

def test_todos():
    todos.visit()

    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

    todos.edit('b', ' edited')
    todos.toggle('b edited')

    todos.clear_completed()
    todos.should_be('a', 'c')
    todos.edit('c', ' to be canceled')
    todos.delete('c to be canceled')
    todos.should_be('a')


test_todos()
