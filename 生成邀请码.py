# 生成邀请码
# id -> 8 -> add number

import click

@click.command()
@click.option("--id", default='', help= "输入id")
def generate(id):
    eight = str(int(id,8))
    eight = eight + '9'
    temp_eght = list(eight)
    temp = []
    for i in temp_eight:
    # print(i)
    # b = random.choice([1， 2， 3， 4， 5， 6， 7， 8， 9， 0])
        b = random.randint(0,9)
        # print(type(b))
        # a = i*10 + b
        temp.append(i)
        temp.append(b)
        # print(a,b)
    # print(int(temp))
    print(temp)
    strA = ''.join(str(s) for s in temp if s not in [None])

    print(strA)
    # 转化16
    print(int(strA, 16))
    # return int(strA, 16)
    click.echo("Hello {}!".format(strA))

if __name__ == '__main':
    generate()
