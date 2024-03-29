from tests.pages import todos


def test_todos_life_cycle():
    todos.visit()

    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

    todos.edit('b', 'b edited')
    todos.toggle('b edited')

    todos.clear_completed()
    todos.should_be('a', 'c')

    todos.cancel_edit('c', 'c to be canceled')

    todos.delete('c')
    todos.should_be('a')
test_todos_life_cycle()
