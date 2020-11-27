* windows cmd 下  找到python 与 pip 文件存放地址    
```    
λ  where.exe python    
D:\Python36\python.exe    
    
λ  where.exe pip    
D:\Python36\Scripts\pip.exe    
```    
    
* windows 自带ubuntu下 （Windows系统盘符存在`/mnt/`中）    
```shell    
:~$ sudo ln -s /mnt/d/Python36/Scripts/pip.exe /usr/bin/wpip    
:~$ sudo ln -s /mnt/d/Python36/python.exe /usr/bin/wpython    
```    
