import os

def convert_images_to_jpg(target_directory):
    """
    遍歷指定目錄及其所有子目錄，將非 .jpg 的常見圖片檔案重新命名為 .jpg。

    Args:
        target_directory (str): 要處理的目標目錄路徑。
    """
    # 定義常見的圖片副檔名列表（小寫）
    image_extensions = ['.png', '.jpeg', '.bmp', '.gif', '.tiff']
    
    # 檢查目標目錄是否存在
    if not os.path.isdir(target_directory):
        print(f"錯誤：目錄 '{target_directory}' 不存在。")
        return

    print(f"開始掃描目錄：'{target_directory}'...")
    
    # os.walk() 會遞迴地遍歷目錄
    for root, dirs, files in os.walk(target_directory):
        for filename in files:
            # 分離檔名和副檔名
            file_base, file_ext = os.path.splitext(filename)
            
            # 如果副檔名（轉為小寫）在我們的列表中，但不是 '.jpg'
            if file_ext.lower() in image_extensions and file_ext.lower() != '.jpg':
                # 建立原始檔案的完整路徑
                original_path = os.path.join(root, filename)
                
                # 建立新的檔名（副檔名為 .jpg）
                new_filename = file_base + '.jpg'
                new_path = os.path.join(root, new_filename)
                
                try:
                    # 重新命名檔案
                    os.rename(original_path, new_path)
                    print(f"已重新命名：'{original_path}' -> '{new_path}'")
                except OSError as e:
                    print(f"重新命名失敗：'{original_path}'。錯誤：{e}")

    print("\n處理完成。")

if __name__ == '__main__':
    # --- 使用者設定 ---
    # 請將這裡的路徑改為您要處理的資料夾路徑
    # 例如：'C:/Users/YourUser/Desktop/my_images' 或 './tog'
    # 如果腳本和 tog 資料夾在同一層，可以直接使用 './tog'
    target_directory = './tog' 
    
    convert_images_to_jpg(target_directory)
