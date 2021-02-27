from selene.support.conditions import have
from selene.support.shared import browser

todos = browser.all('#todo-list>li')
new_todo = browser.element('#new-todo')


def visit():
    browser.config.hold_browser_open = True
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, "return $._data($('#clear-completed')[0], 'events').hasOwnProperty('click')"))


def add(*args):
    for text in args:
        new_todo.type(text).press_enter()


def should_be(*text):
    todos.should(have.exact_texts(*text))


def start_editing(todo, adding_text):
    todos.element_by(have.exact_text(todo)).double_click()
    return todos.element_by(have.css_class('editing')) \
        .element('.edit').type(adding_text)


def edit(todo, adding_text):
    start_editing(todo, adding_text).press_enter()


def cancel_edit(todo, adding_text):
    start_editing(todo, adding_text).press_escape()


def toggle(todo):
    todos.element_by(have.exact_text(todo)) \
        .element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(text):
    todos.element_by(have.exact_text(text)).hover() \
        .element('.destroy').click()
