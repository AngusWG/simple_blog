# 代替supervisor - gosuv  

# 项目的部署    
    
### 一. 安装gosuv [Git地址](https://github.com/codeskyblue/gosuv)    
    
- 从[这里](https://github.com/codeskyblue/gosuv/releases)下载对应系统的二进制文件    
    
- 测试启动: `gosuv start-server -f`    
    
- 将gosuv的二进制启动文件软链接到系统bin目录  `ln -s gosuv /usr/local/bin`    
    
### 二. 将gosuv安装为linux的系统服务    
    
###### 1.编写`systemd`的单元配置文件 (启动命令ExecStart和启动路径WorkingDirectory酌情修改)    
    
* vim /lib/systemd/system/gosuv.service    
    
```systemd    
[Unit]    
Description=gosuv    
After=syslog.target    
After=network.target    
    
[Service]    
# Modify these two values and uncomment them if you have    
# repos with lots of files and get an HTTP error 500 because    
# of that    
###    
#LimitMEMLOCK=infinity    
#LimitNOFILE=65535    
Type=simple  # 如果要启动的命令是一个daemon进程, 这里的值设置为forking    
User=root    
Group=root    
# 可以将gosuv链接到bin目录或者直接移动到bin目录    
WorkingDirectory=/usr/local/bin    
# -f 参数指定gosuv前台启动,默认后台启动(如果没有-f参数, 则Type需要改为forking)    
ExecStart=/usr/local/bin/gosuv start-server -f    
Restart=always    
    
# Some distributions may not support these hardening directives. If you cannot start the service due    
# to an unknown option, comment out the ones not supported by your version of systemd.    
ProtectSystem=full    
PrivateDevices=yes    
PrivateTmp=yes    
NoNewPrivileges=true    
    
[Install]    
WantedBy=multi-user.target    
    
```    
    
###### 2. 将此文件放到 `/lib/systemd/system`文件夹下,此时就能够让服务开机启动和自动重启了    
    
- 开机启动: `systemctl enable gosuv`    
- 启动服务: `systemctl start gosuv`    
- 浏览器中访问: `localhost:11313`    
    
