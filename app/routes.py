# routes dina use garni function lai flask ma
# view function vandao raichha,controller jastai.

from app import x


@x.route('/')
@x.route('/index')
def index():
    return "Hello World"
