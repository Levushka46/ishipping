import redis

r = redis.Redis(host='127.0.0.1', port=6379)

def get_usd_rub():
    return float(r.get('usd_rub')) if r.get('usd_rub') else None

def set_usd_rub(value):
    r.set('usd_rub', value, ex=900)#15 minute