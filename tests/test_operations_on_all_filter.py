from tests.pages.todos import todomvc


def add():
    todomvc().visit()\
        .add('a', 'b', 'c')
    todomvc().should_be('a', 'b', 'c')


def edit():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .edit('b', 'b edited')
    todomvc().should_be('a', 'b edited', 'c')


def cancel_editing():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .cancel_editing('c', 'c to be canceled')
    todomvc().should_be('a', 'b', 'c')


def complete_one():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .complete('b')
    todomvc().should_be_completed('b')
    todomvc().should_be_active('a', 'c')


def activate_one():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .complete('b')\
        .activate('b')
    todomvc().should_be_active('a', 'b', 'c')


def complete_all():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .toggle_all()
    todomvc().should_be_completed('a', 'b', 'c')


def activate_all():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .toggle_all()\
        .toggle_all()
    todomvc().should_be_active('a', 'b', 'c')


def clear_completed():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .complete('b')\
        .clear_completed()
    todomvc().should_be('a', 'c')


def delete():
    todomvc().given_at_todomvc_with('a', 'b', 'c')\
        .delete('b')
    todomvc().should_be('a', 'c')
