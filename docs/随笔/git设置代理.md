# git设置代理  

https://gist.github.com/laispace/666dd7b27e9116faece6    

## git 设置全局代理

```    
git config --global https.proxy http://127.0.0.1:1080    
git config --global https.proxy https://127.0.0.1:1080    
```

## git 删除全局代理

```
git config --global --unset http.proxy        
git config --global --unset https.proxy    
```

## git 设置只对github的代理

```
git config --global http.https://github.com.proxy socks5://127.0.0.1:9999
```

## git 删除只对github的代理

```
git config --global --unset http.https://github.com.proxy)
```

---

在用户目录下 `~\.gitconfig` 下查看配置

--- 

## pip设置豆瓣源

顺便贴一下 

```
pip config set global.index-url https://pypi.douban.com/simple
```

npm config delete proxy    
