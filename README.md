Visual Taipei
========

如何將此 map 跑起來
--------

1. 安裝 github
  * http://git-scm.com/download/mac

2. 打開 Terminal (終端機)，進到可以開始輸入指令的狀態時，會處在 ```/home``` 的資料夾，建議依序輸入以下指令：
  * ```mkdir project```
  * ```cd project```
  * ```git clone https://github.com/wesley100002001/visual-taipei.git```
    * 執行完之後會看到裡面多了一個資料夾叫 visual-taipei

3. 進入 visual-taipei 資料夾裡，先輸入以下指令確認 python 版本
  * ```python --version```

4. 然後根據版本，在 project 資料夾裡，輸入以下指令：
  * Python 2.x
      * ```python -m SimpleHTTPServer```

  * Python 3.x
      * ```python3 -m http.server```

4. 接著畫面會顯示```Serving HTTP on 0.0.0.0 port 8000 ...```，也就是 python 成功地架起了一個簡單的伺服器，網址叫「0.0.0.0」，port 為 8000，而這個網址又可稱為 localhost，所以我們在瀏覽器打開```http://localhost:8000/```，就可以連進這個伺服器，看到剛剛 clone 下來的檔案，接著直接點開 html 檔，就可以看到完整的地圖。

如何更新 map
-----------
如果 map 有更新，則必須從 github 把新的程式碼抓下來方法如下：

1. 一樣打開 Terminal，先輸入```cd project```進入 ```/home``` 底下的 project 資料夾

2. 輸入 ```git pull```，Terminal 便會開始自動抓取這個 repository 上最新的程式碼。
