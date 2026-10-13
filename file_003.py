import os

def batch_rename_files(folder_path, prefix="", suffix="", start_num=1):
    """
    批量重命名指定文件夹内的文件
    :param folder_path: 目标文件夹路径
    :param prefix: 文件名前缀
    :param suffix: 文件名后缀（不含扩展名）
    :param start_num: 序号起始数字
    """
    if not os.path.isdir(folder_path):
        print(f"错误：{folder_path} 不是有效的文件夹路径")
        return

    file_list = os.listdir(folder_path)
    count = 0

    for index, filename in enumerate(file_list, start=start_num):
        # 跳过文件夹，只处理文件
        file_path = os.path.join(folder_path, filename)
        if os.path.isdir(file_path):
            continue

        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        # 构造新文件名：前缀 + 三位序号 + 后缀 + 原扩展名
        new_name = f"{prefix}{index:03d}{suffix}{ext}"
        new_path = os.path.join(folder_path, new_name)

        # 执行重命名
        os.rename(file_path, new_path)
        print(f"重命名: {filename} -> {new_name}")
        count += 1

    print(f"\n完成！共重命名 {count} 个文件")

if __name__ == "__main__":
    # 示例：重命名当前目录下的文件，前缀为 file_，从 1 开始编号
    target_folder = "./"
    batch_rename_files(target_folder, prefix="file_", start_num=1)