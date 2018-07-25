
# Line-bot-python-simple-starter

## 安裝Line-bot-SDK
```
pip install line-bot-sdk
```

## 說明

本範例改寫於[line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)，較適合初次接觸聊天機器人架設的人使用，並適用於[Heroku](https://www.heroku.com/)的架設環境。

## 運行原理
![](https://i.imgur.com/8Dz81wh.png)

## 檔案敘述

|檔案名稱|功能|
|-|-|
|app.py|Linebot主程式、Flask應用主程式|
|Procfile|成功上架至Heroku後的執行檔案，Heroku將會執行這個檔案內所寫的指令 `python app.py`來執行這主程式|
|requirements.txt|套件需求檔，**所有使用到的外部套件需條列在此檔內**，應用程式上架至Heroku後需透過此檔案替執行環境安裝所需套件|
|readme.md|本說明文件|
|.gitignore|條列不想要被git紀錄的檔案|

## 初次建構的環境需求
需要透過此範例架設Line聊天機器人，必須準備好以下步驟

1. 安裝line-bot-sdk請下`pip install line-bot-sdk`
2. 安裝[Git](https://git-scm.com/)
3. 註冊[Heroku](https://dashboard.heroku.com/)帳號並安裝[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. 註[Line開發者帳號](https://developers.line.me/en/)，並替你的機器人建立頻道
5. 啟用Webhook並取得Channel Secret與Access Token
6. 請將Channel Secret與Access Token寫入app.py文件指定的位置
7. 上架應用程式至Heroku

### 1. 安裝Git

![](https://i.imgur.com/rghIfGS.png)

請至Git的[官方網站](https://git-scm.com/)下載並安裝Git

初次安裝好Git請透過終端機輸入以下指令：
```
git config --global color.ui true
git config --global user.name 你的使用者名稱
git config --global user.email 你的Email
```

### 2. 註冊Heroku帳號並安裝Heroku CLI

![](https://i.imgur.com/p5ciBKT.png)

1. 至[Heroku官方網站](https://dashboard.heroku.com/)註冊使用者帳號
2. 下載[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)並安裝至電腦內
3. 在終端機內輸入指令`heroku login`登入Heroku

### 3. 註冊Line開發者帳號，並替你的機器人建立頻道

1. 前往[Line開發者頁面](https://developers.line.me/en/)點選*Start using messaging API* 並且使用LINE帳號登入
2. 建立或選擇一個Provider
3. 建立一個Channel並輸入相關資訊

### 4. 啟用Webhook並取得Channel Secret與Access Token
1. 點選剛才建立的機器人帳號並進入編輯頁面
2. 在編輯頁面中你可以找到頻道的Channel Secret，並產生一組Access Token
3. 將Channel Secret與Access Token寫入app.py文件指定的位置內
4. 點選Use webhooks並改寫成Enabled，將Webhook URL的對應網址改成 `你的heroku專案名稱.herokuapp.com/callback`

## 初次上架專案至Heroku

### 1. 建立一個Heroku專案

前往[Heroku Dashboard](https://dashboard.heroku.com/apps)並點選右上角的 new -> Create new app，建立一個專案。

### 2. 透過Git上架專案至Heroku

在專案資料夾內，開啟終端機並輸入以下指令：

```
git init
git add .
git commit -m "專案第一次上架"
heroku git:remote -a Heroku的專案名稱
git push heroku master
```

## 更新專案至Heroku

```
git add .
git commit -m "寫入你做的修改"
git push heroku master
```