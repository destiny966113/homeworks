完成時間2週。 (截止日期 0203-02-22)

TODO (prerequisites)
- [x] 申請並設定 Google Cloud Free Trial Account (90天)
- [x] 設定相關 API 存取權限與 credential
- [x] 完成 GA4 關聯帳號存取權限設定
- [x] 記錄 google analytics property id

## 請參考 coding.py
- [x] [程式能力] 請用 Python 實作數學運算字 parser ，並計算其結果。
例： a = "(2+3) * 2"，要得到 10 。

## 請參考 api.py
- [x] [程式能力] 請用 Python-flask 實作一 API Server ，根據 輸入的寬高數值，給予對應大小的 png ，圖片顏色不限，可使用各種 pip 套件。回傳時間需小於0.7秒

- [x] [程式能力] 申請 Google Cloud 免費額度，使用 Google Cloud Logging 紀錄第二題的 API 使用狀況上傳。

- [x] [測試能力] 呈上，請實作 unit testing/e2e testing 。

- [ ] [程式能力與文件串接能力] 承第二題 ，請閱讀 Google Analytics 技術文件，將 API 執行紀錄也寫入 Google Analytics Event 。（參考資料：https://developers.google.com/analytics/devguides/collection/protocol/v1 ）

- [x] [系統評估] RDB/NoSQL DB各有什麼優缺點？
```
RDB 優點是ACID的特性，具有強一致性，所以對 transaction 支持很好，並且適合處理結構化數據、當數據之間有關連性時也能更好的發揮，但相對的缺點就是缺少了彈性。
NoSQL DB 優點是具有非常大的彈性，也容易擴充，適合處理非結構化、半結構化、欄位經常變更的數據，但在處理資料關聯和一致性，就相對不是最佳選擇。
```

- [x] 根據 https://roadmap.sh/backend ，盤點你既有哪些技能。
```
Version Control Systems
Relational Databases
NoSQL Databases
Scaling Databases
Caching
Web Security Knowledge
DevOps 
CI/CD
Web Servers
Nginx
Docker
Redis
Nodejs
Python
gRPC
Authentication
Authorization
OAuth
Access Token
Rrefresh Token
Basic Auth
Token Auth
JWT
```
