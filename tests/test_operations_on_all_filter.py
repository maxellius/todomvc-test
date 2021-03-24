from tests.pages import todos


def test_add():
    todos.visit()

    #WHEN nothing
    todos.add()
    
    todos.should_be_empty_list()

    #WHEN
    todos.add('a')

    todos.should_be('a')
    todos.items_left_should_be(1)

    #WHEN
    todos.add('b', 'c')

    todos.should_be('a', 'b', 'c')
    todos.items_left_should_be(3)


def test_edit():
    todos.visit_with('a', 'b', 'c')

    todos.edit('b', 'b edited')

    todos.should_be('a', 'b edited', 'c')
    todos.items_left_should_be(3)


def test_edit_by_focus_change():
    todos.visit_with('a', 'b', 'c')

    todos.edit_by_tab('b', 'b edited')

    todos.should_be('a', 'b edited', 'c')
    todos.items_left_should_be(3)


def test_cancel_editing():
    todos.visit_with('a', 'b', 'c')

    todos.cancel_editing('c', 'c to be canceled')

    todos.should_be('a', 'b', 'c')
    todos.items_left_should_be(3)


def test_complete_one():
    todos.visit_with('a', 'b', 'c')

    todos.toggle('b')

    todos.should_have_completed('b')
    todos.should_have_active('a', 'c')
    todos.items_left_should_be(2)


def test_activate_one():
    todos.visit_with('a', 'b', 'c')
    todos.toggle_all()

    todos.toggle('b')

    todos.should_have_active('b')
    todos.should_have_completed('a', 'c')
    todos.items_left_should_be(1)


def test_complete_all():
    todos.visit_with('a', 'b', 'c')

    todos.toggle_all()

    todos.should_have_completed('a', 'b', 'c')
    todos.should_have_active()
    todos.items_left_should_be(0)


def test_activate_all():
    todos.visit_with('a', 'b', 'c')
    todos.toggle_all()

    todos.toggle_all()

    todos.should_have_active('a', 'b', 'c')
    todos.should_have_completed()
    todos.items_left_should_be(3)


def test_clear_completed():
    todos.visit_with('a', 'b', 'c', 'd')
    todos.toggle('b')
    todos.toggle('d')

    todos.clear_completed()

    todos.should_be('a', 'c')
    todos.items_left_should_be(2)


def test_delete():
    todos.visit_with('a', 'b', 'c')

    #WHEN
    todos.delete('b')
    todos.should_be('a', 'c')
    todos.items_left_should_be(2)

    #WHEN
    todos.delete('a')
    todos.delete('c')
    todos.should_be_empty_list()
