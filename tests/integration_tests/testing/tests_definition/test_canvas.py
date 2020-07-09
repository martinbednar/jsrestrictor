from values_getters import is_canvas_spoofed


## Test canvas - if canvas is spoofed: Reading from canvas returns white image.
def test_canvas(browser, expected):
    try:
        is_spoofed = is_canvas_spoofed(browser.driver)
    except:
        print("\nCan not read Canvas data.")
        assert False
    else:
        if expected.protect_canvas:
            assert is_spoofed
        else:
            assert not is_spoofed
