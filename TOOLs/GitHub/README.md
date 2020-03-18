# GitHub

- [Initialize Setting](#initialize-setting)
- [How To use](#how-to-use)
    - [Create Local Repository](#create-local-repository)
    - [Push](#push)
    - [Pull](#pull)
    - [Branch](#branch)
    - [Reset](#reset)
    - [Others](#others)

## Initialize Setting
```sh
# ユーザー名とメールアドレスの登録
git config —-global user.name <ユーザー名>
git config —-global user.email <メールアドレス>

# 登録内容確認 .gitconfigファイルの内容を表示
git config --global --list
```

## How To use
### Create Local Repository
```sh
# ローカルリポジトリの作成
git init

# リモートリポジトリの登録
git remote add origin <URLアドレス>
```
### Push
```sh
git add <ファイル名>		# ステージング
git commit -m "コメント"	# コミット
git push origin <ブランチ名>	# プッシュ
```
### Pull
```sh
git fetch   # リモートリポジトリの変更をローカルに引っ張ってくる
git merge <remote-branch>

# 以下でも可能
git pull origin <branch名>
```
### Branch
```sh
git switch <branch>		# ブランチの切り替え
git switch -c <branch>	# ブランチを新規作成して切り替え
git restore <filename>	# ファイルの変更を取り消す

# 特定ファイルを特定のコミットの状態にする
git restore --source <commit> <filename>

# ステージングエリアにあるファイルを復旧する(実ファイルへの変更はそのまま)
git restore --staged <filename>

# ワークツリー上のファイルを復旧する
git restore --worktree <filename>
```
### Reset
```sh
# addの取り消し
git reset HEAD <ファイル名>

# commitの取り消し
git reset --hard HEAD^
# --hard：コミット取り消した上でワークディレクトリの内容も書き換えたい場合
# --soft：ワークディレクトリの内容はそのままでコミットだけを取り消したい場合
# HEAD^：直前のコミット
# HEAD~{n} ：n個前のコミット

# commitの打ち消し
git revert <コミットのハッシュ値>

# pushの取り消し
git reset --hard <戻したいコミットのハッシュ値>
git push -f
```
### Others
```sh
git clone <URL>     # リモートリポジトリをローカルにクローン
git status          # ローカルの変更を確認
git diff <ファイル名>
git log
git show <コミットのハッシュ値> # 指定したコミットの編集箇所をみる
git diff <ブランチ名> <ブランチ名>  # ブランチ同士を比較
git stash
git stash list
git stash apply <stash名>

# ファイルを指定のコミットまで戻す
git checkout <コミットのハッシュ値> <ファイル名>
```