def process_data(func):
    def inner(*args):
        scores=func(*args)
        filtered=list(filter(lambda x:x>=40,scores))
        bonus=list(map(lambda x:5+x,filtered))
        result=sorted(bonus,reverse=True)
        return result
    return inner
@process_data
def calculate_scores(*args):
    return list(args)
scores=calculate_scores(50,40,30,90,90,100,60)
print(scores)
