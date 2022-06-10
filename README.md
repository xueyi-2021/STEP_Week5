# STEP Week5 Homework

Travelling Salesman Problem

#### 方針

- solver_greedy.pyを基づいて、2-optを実装する -> **solver_2-opt.py**
  - 経路と経路は交差しないようにする
  - 2つの直線の交差点を計算するのが大変そう……
  - 結果は交換するかどうかなので、交換した後の距離と交換しない時の距離を比較して小さいのすれば、交差点を計算する必要がなくなる
  - 計算量について、O(n^2)の二重ループ何回するかわからない、めちゃくちゃでかいことしかわからない
    - なお、どのノードから短いのかわからないの全て(5と6は部分)のノードを始点として1回計算するので、計算時間ほんとに長い
      - 毎回計算する時、計算しながら今の最短距離と比較する。もし計算の途中で最短距離より長いなら、このノードからの経路は意味ないことを示すので、breakして次のノードからの経路を計算するっていう方法は計算時間をちょっと短くする（実装してない）
      - またはランダムで始点を選ぶ

<br>

#### 結果

- input_0.csv: 3291.6217214092458
- input_1.csv: 3832.290093905199
- input_2.csv: 4494.417962262893
- input_3.csv: 8256.552416639337
- input_4:csv: 10885.948373534135
- input_5.csv: 21039.853719054645（0から間隔5で探した一番小さい距離）  -> 20932.861101374336（全てのノードを始点としと探した一番小さい距離）
- input_6.csv: 42083.84376329958

<br>

#### 補足みたいなもの

- ファイルの出力の処理まだしてない、ただ最短距離を計算して出力した