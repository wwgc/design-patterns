# coding=utf-8


def boldWrapper(func):
    def wrapper(*args, **kwargs):
        return "<b>{}</b>".format(func(*args, **kwargs))

    return wrapper


class TextTag:

    def __init__(self, text):
        self._text = text

    @boldWrapper
    def render(self):
        return self._text


if __name__ == '__main__':
    text_tag = TextTag("hello, world!")
    print(text_tag.render())
