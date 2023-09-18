def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query)
    result = {key: value[0] for key, value in query_params.items()}
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {
        'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {
        'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=John&age=30&gender=male') == {
        'name': 'John', 'age': '30', 'gender': 'male'}
    assert parse('http://example.com/?param1=value1&param2=value2') == {
        'param1': 'value1', 'param2': 'value2'}
    assert parse('https://example.com/path/to/page?name=Alice&city=New+York') == {
        'name': 'Alice', 'city': 'New York'}
    assert parse('https://example.com/path/to/page') == {}
    assert parse('https://example.com/path/to/page?category=electronics&brand=Samsung') == {
        'category': 'electronics', 'brand': 'Samsung'}
    assert parse('https://example.com/path/to/page?empty=') == {'empty': ''}

    print("All parse tests passed!")


def parse_cookie(query: str) -> dict:
    cookie_dict = {}
    if query:
        pairs = query.split(';')
        for pair in pairs:
            key, value = pair.strip().split('=')
            cookie_dict[key] = value
    return cookie_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {
        'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('key1=value1;key2=value2;key3=value3;') == {
        'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    assert parse_cookie('username=John;email=john@example.com;') == {
        'username': 'John', 'email': 'john@example.com'}
    assert parse_cookie('color=red;size=large;') == {
        'color': 'red', 'size': 'large'}
    assert parse_cookie(
        'city=New+York;country=USA;') == {'city': 'New+York', 'country': 'USA'}
    assert parse_cookie('name=Alice;occupation=teacher;') == {
        'name': 'Alice', 'occupation': 'teacher'}
    assert parse_cookie('id=12345;status=active;') == {
        'id': '12345', 'status': 'active'}

    print("All parse_cookie tests passed!")
