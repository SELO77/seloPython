# AWS LAMBDA FNC
def lambda_handler(event, context):
    name = event.get('name')
    print timeit.default_timer()
    return "hello %s"%name
