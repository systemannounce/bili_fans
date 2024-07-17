from collections import defaultdict


def extract_names_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        names = content.split(',')
        names = [name.strip() for name in names]  # 去除名字两端的空格
    return names


def count_names_infiles(file_path):
    name_counts = defaultdict(int)  # 使用 defaultdict 统计次数
    names = extract_names_from_file(file_path)
    for name in names:
        name_counts[name] += 1
    print(f"共 {len(name_counts) - 1} 个不重复粉丝。")
    return len(name_counts) - 1


file_path = './temp.txt'

if __name__ == '__main__':
    count_names_infiles(file_path)
    pass
