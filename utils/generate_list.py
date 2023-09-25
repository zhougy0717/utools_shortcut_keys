import os
import argparse


def get_js_list(folder):
    out_files = []
    # 遍历目录
    for root, dirs, files in os.walk(folder):
        # 遍历文件
        for file_name in files:
            file_path = "{}/{}".format(root, file_name)
            out_files.append(file_path)
    return out_files


def generate_js_code(file_list):
    import datetime

    # 获取当前日期和时间
    now = datetime.datetime.now()

    # 格式化日期和时间为字符串
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

    comment_head = '''
// This file is generated by a python parser, because I don't know how to read a config file during utools runtime.
// Date {}
    '''.format(formatted_time)
    init_text = '''let shortcuts = []
for (k in shortcutTable) {
    if (utools.isMacOs()) {
        if (k.includes('windows')) {
            continue
        }
    }
    else {
        if (k.includes('macos')) {
            continue
        }
    }
    shortcuts = shortcuts.concat(shortcutTable[k])
}
module.exports = shortcuts'''
    table_text = generate_shortcuts_table(file_list)
    code_text = "{}\n\n{}\n\n{}".format(comment_head, table_text, init_text)
    return code_text


def generate_shortcuts_table(file_list):
    var_lines = []
    table_lines = ["let shortcutTable = {"]
    for f in file_list:
        filename, ext = os.path.splitext(os.path.basename(f))
        var_name = filename
        if f.startswith("../"):
            f = f.replace("../", "./")
        var_lines.append("const {} = require('{}')".format(var_name, f))
        table_lines.append("    {}: {},".format(var_name, var_name))
    table_lines.append("}")
    table_text = "\n".join(table_lines)
    var_text = "\n".join(var_lines)
    return "{}\n\n{}".format(var_text, table_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', type=str, help='输入js文件路径')
    parser.add_argument('-f', '--file', type=str, help='输出目标文件，不输入，则在本地输出shortcuts.js')
    args = parser.parse_args()

    folder_path = args.dir if args.dir is not None else "./json"
    output_file = args.file if args.file is not None else "./shortcuts.js"

    file_list = get_js_list(folder_path)
    text = generate_js_code(file_list)
    with open(output_file, 'w') as of:
        of.write(text)

    print("everything awesome😄")
