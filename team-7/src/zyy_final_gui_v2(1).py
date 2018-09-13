import datetime
import xlrd
import xlwt
from tkinter import Tk, Label, Entry, StringVar, Button, messagebox
from tkinter.filedialog import askopenfilenames, asksaveasfile


# 这里是一个函数的定义，以下的函数也类似，可以参照c语言的函数定义与使用，但在python中，没有void和int区别，python的
# 函数默认是有返回值的，如果没有写return语句，则调用了这个函数后会返回一个None，可以把它理解为c语言里面的NULL
# 在函数的定义过程中，如果需要对某些值设置默认值，可以使用参数名后接值的方式，这个参数就变为了可选参数，如果在调用的过程中没有
# 传入值，则使用当前函数设置的默认值
def excel_to_list(path, start_row=0):
    """
    通过路径把excel读取为二维的List，这个函数可以简化一些对excel的操作
    :param path: 文件路径
    :param start_row: 开始行，默认值是从第0行开始
    :return:二维列表
    """
    # 这里是使用xlrd模板对excel文件进行读取，并取第一个工作薄中的值
    table = xlrd.open_workbook(path).sheets()[0]
    # 这是一个暂时使用的list,其中关于list的定义使用[],字典的定义使用{}
    temp_list = []
    # 这里是使用range函数把excel里面的对应行的索引迭代出来，range函数默认是从0开始，如果只传入一个参数，如：
    # range(10),则相当于range(0,10),会生成这样的一个列表：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # table.nrows表示把excel中的有效行读取出来
    for index_i in range(start_row, table.nrows):
        # list可以使用append进行数据的追加操作，append会把数据链接到这个列表的尾部
        # table.row_values(index)表示读取excel表中的第index行，并返回一个list
        temp_list.append(table.row_values(index_i))
    # return和c语言中的使用类似
    return temp_list


# 这个函数可以参考上一个函数，但这个函数没有把整个表读取出来，只是读取了索引对应的行
def read_excel_row(path, rowindex):
    """
    读取excel里面的某一行数据，返回一个List
    :param path:文件路径
    :param rowindex:行索引
    :return:行索引对应的list
    """

    table = xlrd.open_workbook(path).sheets()[0]
    return table.row_values(rowindex)


def write_list_to_excel(list, path):
    """
    把二维列表写入到excel
    :param list: 二维列表
    :param filename: 文件名
    :return: None
    """
    # 这里是对excel进行写操作，下面的语句表示创建一个空的excel表，并指定它的默认编码为utf-8编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 添加一个新的工作薄，这个工作薄的名称为sheet1
    worksheet = workbook.add_sheet('sheet1')
    # 对传入的二维列表进行迭代处理，enumerate函数可以把list的值和索引都迭代出来，因为这里要对excel的单元格进行操作，做需要用到索引
    for index_i, l_1 in enumerate(list):
        for index_j, l_2 in enumerate(l_1):
            # 把二维列表中的对应索引的值写入到excel中
            worksheet.write(index_i, index_j, label=l_2)
    # 保存excel
    workbook.save(path)


def get_result(result_list, dest_file, title_row, start_row):
    """
    得到合并后的结果
    :param excel_dir:
    :return: None
    """
    print('获取合并后的结果...')
    # 使用一个空的list去盛装合并后的数据
    excel_list = []
    # 表示加excel的标题，把用户指定的标题行读取出来，放在list的第一行
    # os.path.json表示把两个路径连在一起，返回值为一个新的路径
    excel_list.append(read_excel_row(result_list[0], title_row))
    for file in result_list:
        # 迭代所有文件，实质是文件名，files是一个当前文件夹下文件名的list
        # 这里把每一个excel文件读取出来，读取的excel数据为从用户指定的开始行开始，并把读取后的这个list转换为二维列表
        temp_excel = excel_to_list(file, start_row)
        # 迭代当前这个excel的二维数据，得到的是excel的每一行，每一行都是一个一维的list
        for t in temp_excel:
            # 把当前的这个excel的每一行都加到总的list中
            excel_list.append(t)
    # 调用把二维列表写入到excel的函数，把这个合并后的二维list写入到用户指定的输出目录中，当把合并后的excel文件名定义为result.xls
    write_list_to_excel(excel_list, dest_file)
    # 打印出一些提示信息
    # print('合并完毕，输出路径为{}'.format(dest_dir))
    show_msgbox('提取并合并完毕，输出路径为{}'.format(dest_file))


# 让窗体居中
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


# 展示提示信息
def show_msgbox(text):
    messagebox.showinfo('提示', text)


# 新建一个窗体
form_main = Tk()
# 设置标题
form_main.title('excel文件提取器')
title_row, start_row = StringVar(), StringVar()


def execute():
    # 不为空判断
    if title_row.get() == '':
        show_msgbox('标题行的索引不能为空')
        return
    if start_row.get() == '':
        show_msgbox('开始行的索引不能为空')
        return
    result_list = askopenfilenames(title='选择excel文件，多选', filetypes=[('excel文件', '*.xlsx;*.xls')])
    if len(result_list) == 0:
        show_msgbox('未选择文件')
        # print('无法提取出文件，故无法执行合并操作')
        return
    # 如果选择了文件，则选择保存文件的路径
    save_path = asksaveasfile(title='选择保存文件的路径', filetypes=[('excel文件', '*.xls')],
                              initialfile='导出{}.xls'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    # 获取合并后的结果
    try:
        get_result(result_list, save_path.name, int(title_row.get()), int(start_row.get()))
    except Exception as e:
        # 异常提示
        show_msgbox(str(e))


if __name__ == '__main__':
    # 设置标题行索引的默认值为0
    title_row.set(0)
    # 设置开始行的索引的默认值为0
    start_row.set(1)
    # 指定窗体的大小并使窗体居中
    center_window(form_main, 300, 200)

    # 绘制控件
    Label(form_main, text='标题所在行').grid(row=0, column=0, padx=10, pady=10)
    Entry(form_main, textvariable=title_row).grid(row=0, column=1, padx=10, pady=10)
    Label(form_main, text='开始行').grid(row=1, column=0, padx=10, pady=10)
    Entry(form_main, textvariable=start_row).grid(row=1, column=1, padx=10, pady=10)
    Button(form_main, text='选择excel文件并导出', command=execute).grid(row=2, column=1, padx=10, pady=10)
    use_info = """
    第一步，打开excel所在文件夹，可以多选，在window操作系统中，按住ctrl，鼠标点击可以多选。
    第二步，打开保存文件对话框，可选择输入保存文件的名字和路径，默认会有一个路径填充到文件对话框中。
    说明：标题所在行为要合并的excel的标题所在行，指定后程序会把这个标题提取出来做为excel的头标题，
    开始行为这些excel要从哪一行开始提取，提取直至有效行，
    Excel第一行参数为0，第二行参数为1，以此类推。
    """
    Button(form_main, text='使用说明', command=lambda: messagebox.showinfo('使用说明', use_info)).grid(row=2, column=0, padx=10,
                                                                                               pady=10)
    form_main.mainloop()
