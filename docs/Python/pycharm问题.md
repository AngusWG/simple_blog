按ctrl+V不能贴贴，ctrl+C能复制    
    
选中文字后按Backspace不是删除，而是选定行往后继续+1    
    
原因：Pycharm启动了Vim编辑模式    
    
解决方式：Tools -Vim Emulator  关闭就行了    
    
    
    
字典中，用变量名.get(key1) 和 变量名[key1]的区别    
    
变量名.get(key1)如果没有给0值    
    
变量名[key1]没有则抛出KeyError异常    
