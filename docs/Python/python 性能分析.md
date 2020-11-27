# 相关资料    
[Python 优化第一步: 性能分析实践](https://juejin.im/entry/5873a216a22b9d00589c25e0)    
    
# 安装依赖    
```bash    
pip install pstats    
pip install snakeviz    
```    
---    
# 获取程序运行数据    
```python    
def run_1():    
    """your function """    
    pass    
    
    
def profile_func(func):    
    import cProfile    
    file_name = "prof_{}_1.txt".format(func.__name__)    
    cProfile.run("{}()".format(func.__name__), file_name)    
    import pstats    
    p = pstats.Stats(file_name).sort_stats("cumtime")    
    # p.print_stats("rqalpha_mod_ricequant_data")    
    p.print_stats("base_position")    
    return p    
    
    
if __name__ == '__main__':    
    p = profile_func(run_1)\    
```    
---    
    
# snakeviz 生成剖面图    
运行目录下 命令行输入：    
`snakeviz prof_run_1_1.txt`    
点击生成的连接 查看柱状剖面图    
![image.png](..\images\7485616-a2c27136267a8bdb.png)    
    
---    
# gprof2dot 时间分析图    
`gprof2dot -f pstats mkm_run.prof | dot -Tpng -o mkm_run.png`    
![image.png](..\images\7485616-50571e9d9a8de77b.png)    
    
    
    
![](..\images\7485616-633f052b4326b4d8.jpg)    
    
