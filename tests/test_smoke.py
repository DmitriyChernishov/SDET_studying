from selene import have, be, by
from selene.support.shared import browser
from selene.support.conditions import have


def test_smoke():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    is_loaded = 'return (Object.keys(require.s.contexts._.defined).length === 39)'
    browser.should(have.script_returned(True, is_loaded))
    browser.element('#new-todo').should(be.enabled).type('a').press_enter()
    browser.element('#new-todo').should(be.enabled).type('b').press_enter()
    browser.element('#new-todo').should(be.enabled).type('c').press_enter()

    browser.all("#todo-list>li").should(have.texts('a', 'b', 'c'))

    browser.all("#todo-list>li").element_by(have.exact_text('b')).element(".toggle").click()

    browser.element(by.link_text("Active")).click()
    browser.all("#todo-list>li").by(be.visible).should(have.texts('a', 'c'))

    browser.element(by.link_text("Completed")).click()
    browser.all("#todo-list>li").by(be.visible).should(have.texts('b'))

    browser.element(by.link_text("All")).click()
    browser.all("#todo-list>li").element_by(have.exact_text('b')).element(".destroy").click()
    browser.all("#todo-list>li").should(have.texts('a', 'c'))

    browser.element(by.text("a")).double_click()
    browser.element(by.text("a")).should(have.css_class(".editing"))
    browser.element(by.css("[data-index='0']")).type(" this field was UPD").press_enter()
    browser.element(by.css("[data-index='0']")).should(have.texts("a this field was UPD"))