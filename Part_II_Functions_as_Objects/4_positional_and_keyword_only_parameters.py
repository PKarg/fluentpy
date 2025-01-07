# One of the gretest python features is the flexibility of handling parameters.
# It's closely related to the use of * and ** operators used to unpack iterables and mappings.
# It can be used in functions to unpack collections into separate arguments.
from cgi import print_environ_usage


# example - tag function that generates HTML

def tag(name, *content, class_=None, **attrs):
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'

# function signature can specify keyword-only arguments
def func_with_kword_only_param(a, *, b):  # every argument after * must be a keyword argument; using * by itself blocks using additional variable positional arguments
    return a, b

if __name__ == '__main__':
    print(tag('br'))  # empty tag with specified name
    print(tag('p', 'hello'))  # tag with content; any number of arguments after first will be captured into *content as a tuple
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))  # keyword arguments not explicitly named in the function signature will be captured into **attrs as a dict
    print(tag('p', 'hello', 'world', class_='sidebar'))  # clas_ parameter can only be passed as a keyword argument
    print(tag(content='testing', name='img', src='test.jpg', alt='test image'))  # keyword arguments can be passed in any order; name can also be passed as a keyword argument
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
    print(tag(**my_tag))  # unpacking a dict into keyword arguments


    # calling a function with keyword-only arguments
    print(func_with_kword_only_param(1, b=2))  # prints (1, 2)
    print(func_with_kword_only_param(1, 2))  # raises TypeError - missing keyword-only argument
