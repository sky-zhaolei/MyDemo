from openpyxl import load_workbook

"""
需求：传入excel文件地址
1、读取表头
2、读取数据
返回表头及数据
返回的数据为列表，列表中每个字段均为一组数据

初始化工作：加载excel文件，并打开指定的表单
"""


class Handle_Excel():

    def __init__(self, file_path, sheet_name):
        self.wb = load_workbook(file_path)       #打开对应路径的excel文件
        self.sh = self.wb[sheet_name]            #打开该文件指定的表

    def read_titles(self):                      #读取表头
        titles = []
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    def read_all_datas(self):                       #读取表头及表头下对应的数据
        data_list = []
        titles = self.read_titles()
        for item in list(self.sh.rows)[1:]:
            values = []
            for index in range(len(item)):
                values.append(item[index].value)
            res = dict(zip(titles, values))
            data_list.append(res)
        return data_list

    def close_excel(self):
        self.wb.close()


if __name__ == '__main__':
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data.xlsx")
    get_datas = Handle_Excel(file_path, "maintainself")
    # print(get_datas.read_titles())
    # print(get_datas.read_all_datas())
    all_datas = get_datas.read_all_datas()
    print(all_datas)
    print(type(eval(all_datas[0]["assert"])["code"]))
