Visual Taipei
========

如何將此 map 跑起來
--------

1. 安裝 github
  * http://git-scm.com/download/mac

2. 打開 Terminal (終端機)，在想要的地方執行 git clone git@github.com:xxxxxx。執行完之後會看到裡面多了一個資料夾叫 visual-taipei
  * git clone 後面那一串網址，可以在這個頁面上方的 SSH 按鈕旁邊找到

3. 進入 visual-taipei 資料夾裡，先輸入以下指令確認 python 版本：python --version。然後根據版本，輸入以下指令：
  * Python 2
      * python -m SimpleHTTPServer

  * Python 3
      * python3 -m http.server

4. 接著在瀏覽器打開：http://localhost:8000/，可以看到剛剛 clone 下來的檔案，直接點開 html 檔
就可以看了。
