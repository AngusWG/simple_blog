# Vim 笔记

推荐一下 vim的视屏学习
[玩转Vim 从放弃到爱不释手 - PegasusWang](https://www.imooc.com/learn/1129)

这是个人对PegasusWang视屏学习笔记
---

a append i insert o open a line below

A append after line I insert before line O append a line above

---

vs vertical split sp split

普通选择 v 选择行 V ctrl + v 方块选择

y 复制

ctrl + h 删除上一个字符 ctrl + w 删除上一个单词 ctrl + u 删除当前行 ctrl + a 跳到开头 ctrl + e 跳到结尾

快速回到最后编辑 gi
---

w/W 移到下一个word/WORD 开头 e/E 下一个word/WORD 结尾 b/B 回到上一个word/WORD 开头 backword

f{char} 移动到char字符上 F{char} 向前搜索 t{char} 移动到char的前面字符上 ;,选择上一个下一个

0 移动到行头 ^移动到行头非空白 $ 移动到行尾 g_移动到行尾非空白

() 在句子间移动 {} 在段落间移动

:help 查看帮助

gg/G 移动到文件开头和结尾 ctrl+o 快速返回 H/M/L 跳到屏幕的 Head / Middle / Lower Ctrl +u / Ctrl +f 上下翻页 upword / forward zz 把当前行设置为屏幕中间

---

d 配合使用删除一个单词 x 删除一个字符

dw 删除单词光标及之后的 daw 删除单词包括之后的空格 diw 删除单词

r replace 替换一个字符 R 不断替换 s substitute 插入模式 S 整行删除进入插入模式 c change c t {char} 删除 到 char 并进入插入模式

/ or ? 向前向后搜索 n/N 上一个 下一个匹配

* # 向前向后匹配 直接搜索当前光标的单词

---

vim替换命令
:[range] s[ubstitute]/{pattern}/{string}/[flags]
range表示范围 比如 :10, 20 表示10-20行, %表示全部 pattern是要替换的模式，string是替换后文本 Flags有几个常用的标志 g(global) 表示全局范围内执行 c(confirm) 表示每次确认 n
报告匹配的到的次数而不替换 可以用来查询匹配次数
---

vim 复制粘贴与寄存器

normal模式下复制粘贴： y(yank)复制 p(paste)粘贴 d 删除 使用 d和p 组合可以达到剪切的效果

visual模式下选择，normal模式下再使用p粘贴

yiw 复制一个单词 p粘贴 yy 复制一行 p粘贴 dd 删除一行 p粘贴

insert模式下的粘贴 Ctrl+v(Windows)
Cmd+v(MacOs)
鼠标右键-粘贴

---


Ctrl + n / ctrl + p 补全单词 ctrl+x ctrl+f 补全文件名 ctrl +x ctrl +o 补全代码

---

Vim-plug


