import gkeepapi
import json

credential_path = './credential.json'
credential = json.load(open(credential_path))
email = credential["email"]
master_token = credential["master_token"]

keep = gkeepapi.Keep()
success = keep.authenticate(email, master_token)

# ノートの取得(ノートの作成順に)
gnotes = sorted(keep.all(), key=lambda x: x.timestamps.created)

# コンソールへ表示
# for gnote in gnotes:
print("Created timestamps: " + gnotes[0].timestamps.created.strftime('%Y-%m-%d %H:%M:%S'))
print("id   : " + gnotes[0].id)
print("Title: " + gnotes[0].title)
print("Text : " + gnotes[0].text)
print("-------------------------------")

# note = keep.createNote('Todo', 'Eat breakfast')
# note.pinned = True
# note.color = gkeepapi.node.ColorValue.Red
# keep.sync()