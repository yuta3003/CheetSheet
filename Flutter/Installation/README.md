# Installation

- [Operating Environment](#operating-environment)
- [Flutter SDK](#flutter-sdk)
    - [Download](#download-flutter-sdk)
    - [Install](#install-flutter-sdk)
- [Android SDK](#android-sdk)
    - [Download and Install](#download-and-install-android-sdk)
    - [Install](#install-android-sdk)
    - [Create Android Emulator](#create-android-emulator)
- [iOS SDK](#ios-sdk)
    - [Install Xcode](#install-xcode)
    - [Setting Xcode command-line tools](#setting-xcode-command-line-tools)



## Operating Environment
|カテゴリ|詳細|
| --- | ---|
| OS  | MacOS|
|ディスク容量|700 MB|
|Third Party Tools|bash, mkdir, rm, git, curl, unzip, which|

## Flutter SDK
### Download Flutter SDK
[公式サイト](https://flutter.dev/)からダウンロードする

### Install Flutter SDK
```sh
cd ~/Library/Developer
unzip ~/Downloads/flutter_macos_v1.12.13+hotfix.8-stable.zip
```
unzip後にPATHを設定
```sh:.zprofile
vim ~/.zprofile
export FLUTTER_HOME="$HOME/Library/Developer/flutter"
PATH="$FLUTTER_HOME/bin:$PATH"
export PATH
```

Run FlutterDoctor
```sh
flutter docter
```

## Android SDK
### Download and Install Android SDK
[公式サイト](https://developer.android.com/studio/)からダウンロード  
初回起動時の指示に従い設定する  

### Create Android Emulator
プロジェクトを作成  
[Tools] -> [AVD Manager]を選択  
[+Create Virtual Device]をクリック
下記コマンドを実行してAndroidのライセンスに同意する
```sh
flutter doctor --android-licenses
```

## iOS SDK
### Install Xcode
App Storeからダウンロード

### Setting Xcode command-line tools
```sh
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer from the command line.
```
```sh
sudo xcodebuild -license from 
```
Xcodeを起動する
