# 国内 github 慢  

### 在hosts文件中加入如下几句即可：    
- vim /etc/hosts   **linux**    
- vim  C:\Windows\System32\drivers\etc\hosts  **windows**    
```    
192.30.252.123 www.github.com    
103.245.222.133 assets-cdn.github.com    
185.31.18.133 avatars0.githubusercontent.com    
185.31.19.133 avatars1.githubusercontent.com    
```    
### 现在这个IP似乎也不管用了，所以如果使用了shadowsocks的可以用git使用代理    
```    
git config --global http.proxy socks5://127.0.0.1:9999    
git config --global https.proxy socks5://127.0.0.1:9999    
```    
用完记得关上，不然内网的git也会很慢    
```    
git config --global --unset http.proxy    
git config --global --unset https.proxy    
```    
    
     
