from expert_fishstick.main import get_item_component

def test_component():
    result = get_item_component("item_text")
    expected = """
        <li>
        <form action="/items" method="post" style="display:inline">
            <input type="hidden" name="item_del" value="item_text">
            <input type="submit" value="Mark Complete">
            <span>item_text</span>
        </form>
        </li>
    """

    assert result==expected


def test_bad_component():
    result = get_item_component("<h1>Cedric</h1>")
    expected = """
        <li>
        <form action="/items" method="post" style="display:inline">
            <input type="hidden" name="item_del" value="<h1>Cedric</h1>">
            <input type="submit" value="Mark Complete">
            <span><h1>Cedric</h1></span>
        </form>
        </li>
    """

    assert result==expected




    