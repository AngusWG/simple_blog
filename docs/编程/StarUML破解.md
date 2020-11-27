https://blog.csdn.net/the_victory/article/details/52781357    
https://blog.csdn.net/the_victory/article/details/52781357    
https://blog.csdn.net/the_victory/article/details/52781357    
    
    
1.  首先打开你的starUML安装目录，并找到LicenseManagerDomain.js,starUML是用NodeJS写的，这个文件就是判断注册用户的文件，我的目录是:`D:\Program Files (x86)\StarUML\www\license\node\LicenseManagerDomain.js`    
2.  修改该文件，找到第24行，加入如下所示区域的代码。    
    
```    
    function validate(PK, name, product, licenseKey) {    
        var pk, decrypted;    
    
        //edit by ChrisChang,加入如下几行    
        return {    
        name: "Chang",//随意    
        product: "StarUML",    
        licenseType: "vip",    
        quantity: "blog.csdn.net/the_victory",//随意    
        licenseKey: "later equals never!"    
        };    
        //-------------END    
    
        try {    
            pk = new NodeRSA(PK);    
            decrypted = pk.decrypt(licenseKey, 'utf8');    
        } catch (err) {    
            return false;    
        }    
        var terms = decrypted.trim().split("\n");    
        if (terms[0] === name && terms[1] === product) {    
            return {    
                name: name,    
                product: product,    
                licenseType: terms[2],    
                quantity: terms[3],    
                licenseKey: licenseKey    
            };    
        } else {    
            return false;    
        }    
    }    
    
```    
    
1.  重启starUML需要在help->Enter License选项里面输入你代码里写的name和licensekey。    
2.  重启starUML，你会发现已经没有提示了，然后点击help->about starUML,结果如下     
    ![这里写图片描述](http://upload-images.jianshu.io/upload_images/7485616-f2b845312cd1035c?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)    
