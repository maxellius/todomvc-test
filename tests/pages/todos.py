from selene import have
from selene.support.shared import browser


be_class_completed = have.css_class('completed')


class todomvc:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')
        self.new_todo = browser.element('#new-todo')

    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        script = "return 'click' in $._data($('#clear-completed')[0],'events')"
        browser.wait_until(have.js_returned(True, script))
        return self

    def visit_with(self, *texts: str):
        self.visit()
        for text in texts:
            self.new_todo.type(text).press_enter()
        return self

    def add(self, *texts: str):
        for text in texts:
            self.new_todo.type(text).press_enter()
        return self

    def should_be(self, *texts: str):
        self.todo_list.should(have.exact_texts(*texts))
        return self

    def should_be_empty(self):
        self.todo_list.should(have.size(0))
        return self

    def should_have_items_left(self, amount: int):
        browser.element('#todo-count>strong')\
            .should(have.exact_text(str(amount)))
        return self

    def start_editing(self, text: str, new_text: str):
        self.todo_list.element_by(have.exact_text(text)).double_click()
        return self.todo_list.element_by(have.css_class('editing'))\
            .element('.edit').with_(set_value_by_js = True).set_value(new_text)

    def edit(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_enter()
        return self

    def edit_by_tab(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_tab()
        return self

    def cancel_editing(self, text: str, new_text: str):
        self.start_editing(text, new_text).press_escape()
        return self

    def toggle(self, text: str):
        self.todo_list.element_by(have.exact_text(text))\
            .element(".toggle").click()
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def list_should_have_completed(self, *texts: str):
        self.todo_list.filtered_by(be_class_completed)\
            .should(have.exact_texts(*texts))
        return self

    def list_should_have_active(self, *texts: str):
        self.todo_list.filtered_by(be_class_completed.not_)\
            .should(have.exact_texts(*texts))
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def delete(self, text: str):
        self.todo_list.element_by(have.exact_text(text)).hover()\
            .element(".destroy").click()
        return self
