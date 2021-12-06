import json


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_tags(data):
    results = set()

    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results


def add_post(filename, post):
    data = read_json(filename)
    data.append(post)
    
    with open(filename, 'w', encoding='utf-8') as f:
         json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


def get_posts_by_tag(data, tag):
    result = []
    for record in data:
        if f'#{tag}' in record['content']:
            result.append(record)
    return result