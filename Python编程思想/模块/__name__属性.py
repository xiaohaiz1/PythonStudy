''''''
import template
'''
__name__属性：
模块就是一个可执行的.py文件，一个模块被另一个程序引入，我不想让模块中的某些代码
执行，可以用__name__属性来使程序仅调用模块中的一部分
对于一个py模块文件如果不使用__name__属性，那么会从上往下依次执行，浪费资源

从这个程序可以看出，我调用模块文件时，不仅调用了函数，还执行了全部

因此在每一个模块文件中都有一个__name__属性，当其值等于"__main__"时，表明该模块自身在执行。
当这个程序在执行时__name__属性就会变为"__main__",那么当他不是在执行的文件时而是被调用的话则不会执行if里的语句
所以我们可以将py文件的if里的语句看成主函数当被调用时则不会执行里面的，但自己运行时也可以按照主函数进行下去，
加入这个属性进去，既可以将其当成主程序用，又可以不影响的当成模块用

'''
template.sayGood()