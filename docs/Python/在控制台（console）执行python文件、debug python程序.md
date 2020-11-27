# 执行    
在IPython console里先cd到test.py所在的文件夹，再run test.py。注意使用的是命令run 而不是命令python。    
# debug    
栗子：    
```    
debugfile('/home/1/tensor2tensor/tensor2tensor/bin/t2t-datagen', args='--problem=image_mnist --data_dir=~/t2t_data --tmp_dir=~/t2t_data/tmp',wdir='/home/1/tensor2tensor/tensor2tensor/bin')    
```    
    
* ipython下    
    
```python    
cd /home    
pwd    
ls    
help(runfile)    
Help on function runfile in module _pydev_bundle.pydev_umd:    
runfile(filename, args=None, wdir=None, is_module=False, global_vars=None)    
    Run filename    
    args: command line arguments (string)    
    wdir: working directory    
run test.py     
```    
    
更多资料    
https://www.jianshu.com/p/63175f02749b    
