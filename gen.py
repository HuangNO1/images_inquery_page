import os
import json

def generate_survey_data(base_path="tog"):
    """
    掃描指定的基礎路徑（預設為 'tog'），
    讀取符合 'id-name' 格式的子資料夾，
    並從中提取 id、name 和 prompt.txt 的內容，
    最終生成 survey_data.js 檔案。

    Args:
        base_path (str): 要掃描的基礎目錄路徑。
    """
    survey_list = []
    
    # 檢查基礎路徑是否存在
    if not os.path.isdir(base_path):
        print(f"錯誤：目錄 '{base_path}' 不存在。請確保腳本與 '{base_path}' 目錄在同一層級。")
        return

    print(f"開始掃描目錄：'{base_path}'...")

    # 遍歷基礎路徑下的所有項目
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        
        # 確保是資料夾並且名稱中包含 '-'
        if os.path.isdir(folder_path) and "-" in folder_name:
            try:
                # 分割 id 和 name
                id_str, name = folder_name.split("-", 1)
                
                # 檢查 prompt.txt 是否存在
                prompt_file_path = os.path.join(folder_path, "prompt.txt")
                if not os.path.exists(prompt_file_path):
                    print(f"警告：在 '{folder_name}' 中找不到 prompt.txt，已跳過。")
                    continue

                # 讀取 prompt.txt 內容
                with open(prompt_file_path, "r", encoding="utf-8") as f:
                    prompt = f.read().strip()
                
                # 將結果加入列表
                survey_list.append({
                    "id": int(id_str),
                    "name": name,
                    "prompt": prompt
                })
                print(f"成功處理：'{folder_name}'")

            except ValueError:
                print(f"警告：'{folder_name}' 的 ID 部分不是有效的數字，已跳過。")
            except Exception as e:
                print(f"處理 '{folder_name}' 時發生錯誤：{e}")
    
    # 檢查是否有掃描到任何資料
    if not survey_list:
        print("\n未找到任何有效的問卷資料夾，未生成 survey_data.js。")
        return

    # 將 Python 列表轉換為 JSON 字串
    # indent=2 讓 JSON 格式更美觀
    json_string = json.dumps(survey_list, ensure_ascii=False, indent=2)
    
    # 組合成 JavaScript 變數賦值的完整字串
    js_content = f"const SURVEY_DATA = {json_string};"
    
    # 將內容寫入 survey_data.js
    try:
        with open("survey_data.js", "w", encoding="utf-8") as f:
            f.write(js_content)
        print("\n✅ 已成功生成 survey_data.js")
    except IOError as e:
        print(f"\n❌ 寫入 survey_data.js 失敗。錯誤：{e}")


if __name__ == '__main__':
    # 直接執行此腳本即可
    generate_survey_data()
