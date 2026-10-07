def count_calls(func):
    count=0
    def time(*args,**kwargs):
        nonlocal count
        count+=1
        print(f"Executed {count}times.")
        func(*args,**kwargs)
    return time
@count_calls
def generate_ticket():
    return "ticket123"
generate_ticket()
generate_ticket()
generate_ticket()
generate_ticket()