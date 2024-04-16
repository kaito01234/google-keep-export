import gkeepapi
import json
import os
import sys

# ファイル名に使用できない文字を置換する関数
def sanitize_filename(filename):
    if not filename:  # タイトルが空の場合はファイル名に使用されない
        return None
    return filename.replace("/", "-").replace("\\", "-").replace(":", "-").replace("*", "-").replace("?", "-").replace("\"", "-").replace("<", "-").replace(">", "-").replace("|", "-")

# コマンドライン引数から出力するファイル数を取得、未指定の場合は全件出力
if len(sys.argv) > 1:
    try:
        num_files = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for the number of files to create.")
        sys.exit(1)
else:
    num_files = None  # 引数が指定されていない場合、全件出力

# 認証情報の読み込み
credential_path = './credential.json'
with open(credential_path, 'r') as f:
    credential = json.load(f)
email = credential["email"]
master_token = credential["master_token"]

# Google Keep API の初期化とログイン
keep = gkeepapi.Keep()
success = keep.authenticate(email, master_token)

# ノートの取得 (作成順にソート)
gnotes = sorted(keep.all(), key=lambda x: x.timestamps.created)

# 出力ディレクトリの準備
output_dir = './export'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 指定された数または全ノートの内容をファイルに出力
count = 0
for gnote in gnotes:
    if num_files is not None and count >= num_files:
        break
    # ファイル名を設定 (不正な文字は置換、空の場合はgnote.id使用)
    sanitized_title = sanitize_filename(gnote.title)
    filename = os.path.join(output_dir, sanitized_title + ".md") if sanitized_title else os.path.join(output_dir, gnote.id + ".md")
    
    # ファイルに書き出し
    with open(filename, 'w') as f:
        f.write(gnote.text)

    # ファイル作成の確認出力
    print("Markdown file created: " + filename)
    print("-------------------------------")
    count += 1
