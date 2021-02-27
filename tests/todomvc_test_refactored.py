from todomvc_test.modul import todos


def test_add_complete():
    todos.visit('https://todomvc4tasj.herokuapp.com/')

    todos.add('a', 'b', 'c')
    todos.should_be('a', 'b', 'c')

    todos.edit('b', ' edited')
    todos.toggle('b edited')

    todos.clear_completed()
    todos.should_be('a', 'c')

    todos.cancel_edit('c', ' to be canceled')

    todos.delete('c')
    todos.should_be('a')

test_add_complete()
