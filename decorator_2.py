import datetime
import json

def decorator_maker(path):
    def decorator_logger(func):
        def wrapper(*args, **kwargs):
            dict_for_json = {}
            dt = datetime.datetime.now()
            dict_for_json['date'] = dt.strftime('%d.%m.%Y')
            dict_for_json['time'] = dt.strftime('%H:%M:%S')
            dict_for_json['name'] = func.__name__
            dict_for_json['args'] = args
            dict_for_json['kwargs'] = kwargs
            dict_for_json['result'] = func(*args, **kwargs)
            with open(path, 'a', encoding='utf8') as f:
                print('ok')
                json.dump(dict_for_json, f)
                f.write('\n')
            return dict_for_json['result']
        return wrapper
    return decorator_logger
