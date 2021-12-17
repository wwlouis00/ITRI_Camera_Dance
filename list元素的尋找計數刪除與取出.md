# list元素的新增與串接: insert append extend
```javascript
let num = Math.random();
```


#### 預設 s=[0,1,2]

| 程式 | 結果 | 說明 |
| --- | --- | ---    |
| s.insert(1,9) | s=[0,9,1,2] |在索引1插入9 |
| s.append(3) | s=[0,1,2,3] | 在最後面加入3 |
| s.extend[4,5]) | s=[0,1,2,4,5] | 在最後面串接list |
| s+=[4,5] | s=[0,1,2,4,5] | 同上 |
