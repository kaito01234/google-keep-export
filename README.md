# Goole Keep Export

## 依存関係

### 依存関係のインストール

- `pip install -r requirements.txt`

###  依存関係のエクスポート

- `pip freeze > requirements.txt`

###  アップデートある依存関係の一覧表示

- `pip list -o`

###  依存関係のアップデート

- `pip install gkeepapi==0.16.0`

## 実行

### OAuth Token取得
- googleアカウントにログイン
- cookieからoauth_tokenをコピー

### マスタートークンの取得

- 以下を実行して `Token` を取得

```bash
docker run --rm -it --entrypoint /bin/sh python:3 -c 'pip install gpsoauth; python3 -c '\''print(__import__("gpsoauth").exchange_token(input("Email: "), input("OAuth Token: "), input("Android ID: ")))'\'
```

### credential.json作成

```json
{
  "email": "your email",
  "master_token": "MasterToken"
}
```

### 実行

- `python keep_export.py`
