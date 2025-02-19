# Kai-in - 会員管理システム

会員管理、団体管理、クラブ管理、会費管理などの機能を提供する総合的な会員管理システムです。

## 主な機能

- 会員管理 (Members)
- 団体管理 (Associations)
- クラブ管理 (Clubs)
- 会費管理 (Payments) - Stripe連携
- 認証・権限管理 (Auth)
- ダッシュボード (Dashboard)
- 通知機能
- マイページ

## 技術スタック

- Django
- PostgreSQL
- Docker
- TailwindCSS
- Stripe

## セットアップ方法

1. リポジトリをクローン:
```bash
git clone [repository-url]
cd kai-in
```

2. 環境変数の設定:
`.env`ファイルを作成し、必要な環境変数を設定してください。

3. Dockerでの起動:
```bash
docker-compose up --build
```

4. データベースのマイグレーション:
```bash
docker-compose exec web python manage.py migrate
```

5. 開発用サーバーへのアクセス:
ブラウザで http://localhost:8000 にアクセス

## 開発環境の要件

- Docker
- Docker Compose
- Python 3.11以上（ローカル開発の場合）

## ライセンス

All rights reserved.
