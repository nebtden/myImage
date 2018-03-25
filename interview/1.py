# 补充缺失的代码


def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    import os
    print(os.path.curdir)
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChild):
            for ssChild in os.listdir(sPath):
                print(ssChild)

    # for sChild in os.listdir(sPath):
    #     sChildPath = os.path.join(sPath, sChild)
    #     if os.path.isdir(sChildPath):
    #         print_directory_contents(sChildPath)
    #     else:
    #         print
    #         sChildPath


if __name__=='__main__':
    print_directory_contents("../mnist")
