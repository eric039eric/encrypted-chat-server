# Encrypted Chat Server

> 作者：陳士弘（@eric039eric）
> 完成日期：2025年6月11日

---

## 程式介紹

這是一個基於 Python 與 Socket 網路通信程式，搭配 AES-CBC 加密模式，實現本地區網系統下可以安全通訊的隨話系統，支援中文、英文、多執行線與純程式加密/解密模組。

---

## 目錄結構

```
encrypted-chat-server/
├── .gitignore
├── chat_client.py
├── chat_server.py
├── crypto_helper.py
```

| 檔案                 | 作用                     |
| ------------------ | ---------------------- |
| `chat_server.py`   | 儲存主機端進行 socket 連線並接收密文 |
| `chat_client.py`   | 用戶端程式，可發送訊息並解密回應       |
| `crypto_helper.py` | AES 加密/解密功能模組，擱拔為密碼工具  |
| `.gitignore`       | 用來排除自動生成的 cache/故障檔案   |

---

## 使用教學

### 1. 設備條件

* 兩台裝有 Python 3.x 環境的裝置（手機 Termux 或電腦都可）
* 兩台裝置都在同一區域網 (LAN)上

---

### 2. 啟動 Server 端

```bash
python chat_server.py
```

會顯示：

```
🔐 安全聊天室伺服器已啟動，等待連線...
```

---

### 3. 啟動 Client 端

```bash
python chat_client.py
```

對方線上後，可相互發送、接收加密訊息

---

## 加密技術說明

* **AES (Advanced Encryption Standard)**

  * 加密模式：CBC
  * 鍵長：16 bytes (128 bits)
  * 針對 UTF-8 資料進行 pad/unpad 處理
* **Base64**

  * 用於範圍加密後無法直接連線傳輸的不可覆載字元。

---

## 技術無痕記錄

這個專案是作者在手機 Termux 環境中開發，經歷：

* 本地通訊實例的啟動與對接
* socket 通訊基礎
* AES-CBC 加密與 Base64 轉碼
* Git 分支擋關、rebase 衝突、merge conflict 手動解決
* Termux 轉檔至 PC 處理、GitHub Codespaces 以區分管理

---

## 未來擴充計畫

* 支援兩端用戶同時談天 (multi-client)
* 採用 TLS/公私鑰加密以換掉故式 AES 密鑰
* 建立 GUI (Tkinter/Web) 用戶介面
* 文件傳送與內容加密

---

## 說明

此項目為簡易安全通訊展示，目的為讓學習者理解：

* 密碼作業如何與網絡通訊合併
* 如何解決 Git 實戰中的衝突問題

---

歡迎評價，與提供開發优化建議!
