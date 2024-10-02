def str_int_sum(string: str) -> int:
    bob: int = 0
    for i in string:
        if i.isdigit():
            bob += int(i)
    return bob


print(str_int_sum('-@03,.wdp01./223'))
