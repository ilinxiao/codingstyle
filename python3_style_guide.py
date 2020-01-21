"""Python 提高编码可读性建议

提高项目代码的可读性：
1. 为公共模块，类，函数编写文档说明（Docstrings)。
2. 模块的定义是任何以.py结尾的代码文件被看作是项目中的一个模块，它由函数和类组成。
   仅仅包含函数的模块，文档说明是必须的。这段文字就是模块文档说明。
   包含类定义的模块，类定义较为简单或类和类之间的关系并不复杂，该模块的文档说明可以省略。
3. 类的文档说明是必须的。
4. 这里的函数包括函数(def写在class外面)、方法(def写在class里面)、生成器。函数的文档说
   明应该包含函数做什么, 以及输入和输出的详细描述。非公共的函数没有必要，但是应该有一个
   描述函数具体作用的注释。短小、简单明了的函数可以省略文档说明和注释。
4. 当代码更改时，优先更新对应的文档说明和注释。
3. 用自己熟悉的语言。

-------------------------------------------------------------------
如果你使用IDE工具，建议添加如下设置，自动添加文件头，保持代码风格一致：
Pycharm: File>Settings>File and Code Templates>Python Script

文件头内容参考template文件, 使用前替换自己的信息。
-------------------------------------------------------------------

@author: LX
@contact: lvlinxiao@esoaru.com
@time: 2020/1/21 上午9:27
"""

# 标准库导入
import platform

# 第三方库导入
import redis

# 本地应用库导入
from .tools import excel_tool, img_tool, video_tool

GLOBAL_VARIABLE = "GLOBAL VARIABLE"


class Python3StyleGuide(object):
    """Python 3 编码可读性参考类

    文档说明的格式：
    1. 紧跟申明对象的下一行开始，用成对的连续三个双引号包含说明的内容。
    2. 第一行以三个双引号开始，紧接着写文档说明的主题。主题应该简洁明了用一句话概括申明对象
       的作用。
    3. 文档说明可以只有一行。
    4. 多行文档说明在主题下空出一行空白，详细描述内容对齐第一行的第一个双引号。类说明文档参
       考这段。
    """

    def __init__(self):
        # 初始化类属性
        self._bits = -1

    def get_system_architecture(self, executable, bits: str, linkage=""):
        """获取系统架构

        提取系统的架构信息，返回数字值形式方便项目其他函数调用。
        (在Pycharm中，在函数下面连续输入三个双引号会自动生成以下输入输出说明。)
        :param executable: Python解释器可执行路径
        :param bits: 指定解析器对应的预期系统位数，必须str类型。
        :param linkage: 链接格式，默认值为""。
        :return:
            32 or 64: 32或者64位操作系统
            -1: 系统架构未知
        :raises: 抛出异常说明，没有可以忽略
        """

        # TODO(添加人/指定人) 待做事项格式
        # TODO(LX) 查清楚 architecture 方法第三个参数 linkage 对运行结果的影响

        try:
            # 现有系统接口返回的系统架构信息是由文字形式的系统位数和linkage组成的二元组
            # 格式参考:('64bit', 'ELF')，目的是提取元祖的第一个元素中的数字值

            sys_arch = platform.architecture(executable, bits, linkage)
            sys_arch = int(sys_arch[0].replace("bit", ""))
        except Exception:
            # 部分Unix操作系统中的file命令实现会影响到命令执行结果
            self._bits = -1
        else:
            self._bits = sys_arch

        return self._bits

