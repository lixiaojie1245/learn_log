import os
import datetime
import click


test=False

def get_future():
    # 获取当前目录
    current_directory = os.getcwd()

    dic=current_directory
    if test==True:
        # 获取当前工作目录的父级目录
        parent_directory = os.path.dirname(current_directory)
        dic=parent_directory

    # 获取父目录下的所有项
    entries = os.listdir(dic)


    # 过滤出所有以数字开头的子目录，并排除前6个字符不是数字的目录
    directories = [d for d in entries if os.path.isdir(os.path.join(dic, d)) and d[:6].isdigit()]

    # 对目录列表进行排序
    directories.sort()

    today=datetime.datetime.now()

    todaystr=today.strftime('%y%m%d')
    last=directories[-1][:6]
    n=0
    future= (today + datetime.timedelta(days=n)).strftime('%y%m%d')
    while last >= future:
        future= (today + datetime.timedelta(days=n)).strftime('%y%m%d')
        n+=1

    return future


@click.command()
@click.option('--name', prompt='project name', help='The person to greet.')
def main(name):
    """create a new learn project"""
    dir_name=f"{get_future()}_{name}"
    click.echo(dir_name)

    try:
        os.mkdir(dir_name)
        print(f"目录 '{dir_name}' 创建成功。")
    except OSError as error:
        print(f"创建目录 '{dir_name}' 失败: {error}")

    with open("./sh/source1",'w') as f:
        f.write(f"cd {dir_name}")

    print("use source to move dir")
    print()
    print("source ./sh/source1")
    print()

if __name__ == '__main__':
    main()
        


