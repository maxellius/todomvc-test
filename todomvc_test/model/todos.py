from selene.support.conditions import have
from selene.support.shared import browser

todo_list = browser.all('#todo-list>li')
is_js_loaded = ("return $._data($('#clear-completed')[0], "
                     "'events').hasOwnProperty('click')")


def visit():
    browser.config.hold_browser_open = True
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, is_js_loaded))


def add(*text: str):
    for text in text:
        browser.element('#new-todo').type(text).press_enter()


def should_be(*text: str):
    todo_list.should(have.exact_texts(*text))


def start_editing(old_todo: str, corrected_todo: str):
    todo_list.element_by(have.exact_text(old_todo)).double_click()
    return todo_list.element_by(have.css_class('editing')) \
        .element('.edit').with_(set_value_by_js=True).set_value(corrected_todo)


def edit(old_todo: str, corrected_todo: str):
    start_editing(old_todo, corrected_todo).press_enter()


def cancel_edit(old_todo: str, corrected_todo: str):
    start_editing(old_todo, corrected_todo).press_escape()


def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)) \
        .element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def delete(text: str):
    todo_list.element_by(have.exact_text(text)).hover() \
        .element('.destroy').click()
