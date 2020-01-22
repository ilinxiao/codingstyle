"""Python 提高编码可读性建议 （模块文档说明参考案例）

提高项目代码的可读性：
1. 为公共模块，类，函数编写文档说明（Docstrings)。
2. 模块的定义是任何以.py结尾的代码文件被看作是项目中的一个模块，它由函数和类组成。
   仅仅包含函数的模块，文档说明是必须的。这段文字就是模块文档说明。
   包含类定义的模块，类定义较为简单或类和类之间的关系并不复杂，该模块的文档说明可以省略。
3. 类的文档说明是必须的。
4. 这里的函数包括函数(def写在class外面)、方法(def写在class里面)、生成器。函数的文档说
   明应该包含函数做什么, 以及输入和输出的详细描述。非公共的函数没有必要，但是应该有一个
   描述函数具体作用的注释。短小、简单明了的函数可以省略文档说明和注释。
5. 当代码更改时，优先更新对应的文档说明和注释。一个模块或者类在进行了重大升级之后，比如
   更换了实现框架、请求的方式等，除了补充更新内容以外，根据需要添加更新作者、时间等信息。
6. 用自己熟悉的语言，英文或中文，写文档说明。鼓励多写关于对业务的理解和技术实现细节，一段
   理解不够深的文字，加上具体的没有搞清楚的问题和把具体问题搞清楚之后的文字是等价的。
7. TODO待办清单可以指定创建人和指定人，写在文档说明空一行之后。参考下方示例。
8. 为代码实现的具体细节添加块注释或单行注释。块注释是对某一段代码的实现细节和要处理的问题
   的一个集中解释，它应该写在所要说明的代码块开始行隔一空白行之上，文档说明或其他代码块隔
   一空白行之下。单行注释可以写在要说明的代码上面，中间不能隔空白行;也可以写在代码行后面，
   中间隔两个空格。

-------------------------------------------------------------------
推荐配置：
如果你使用IDE工具，建议添加如下设置，自动添加文件头：
Pycharm: File>Settings>File and Code Templates>Python Script

文件头内容参考pycharm>template.txt文件, 使用前替换自己的信息。

文件头的信息对BUG跟踪会起到一定的帮助，所以只是推荐添加这项配置，并不是必须要求。
-------------------------------------------------------------------

@author: LX
@contact: lvlinxiao@esoaru.com
@time: 2020/1/21 上午9:27
"""

# 标准库导入
import platform
from typing import List

# 第三方库导入
import redis

# 本地应用库导入
from .tools import excel_tool, img_tool, video_tool

GLOBAL_VARIABLE = "GLOBAL VARIABLE"


class PythonStyleGuide:
    """Python 编码可读性参考类 (类文档说明参考案例）

    文档说明的格式：
    1. 紧跟申明对象的下一行开始，用成对的连续三个双引号包含说明的内容。
    2. 第一行以三个双引号开始，紧接着写文档说明的主题。主题应该简洁明了用一句话概括申明对象
       的作用。
    3. 文档说明可以只有一行。
    4. 多行文档说明在主题下空出一行空白，详细描述内容对齐第一行的第一个双引号。类说明文档参
       考这段。
    """

    def __init__(self) -> None:
        # 初始化类属性
        self._bits = -1

    def get_system_architecture(
        self, executable: List[str], bits: str, linkage: str = ""
    ) -> int:
        """获取系统架构 （函数文档说明参考案例）

        提取系统的架构信息，返回数字值形式方便项目其他函数调用。
        (在Pycharm中，在函数下面连续输入三个双引号会自动生成以下输入输出说明。)
        :param executable: Python解释器可执行路径
        :param bits: 指定解析器对应的预期系统位数，必须str类型。
        :param linkage: 系统的连接格式，可选项有["", "ELF", "WINDOWS"]等，默认值为""。
        :return:
            32 or 64: 32或者64位操作系统
            -1: 系统架构未知
        :raises: 抛出异常说明，没有可以忽略
        """

        # TODO(添加人/指定人) 待做事项格式 （TODO参考案例）
        # TODO(LX) 查清楚 architecture 方法第三个参数 linkage 对运行结果的影响

        try:
            # 现有系统接口返回的系统架构信息是由文字形式的系统位数和linkage组成的二元组
            # 格式参考:("64bit", "ELF")，目的是提取元祖的第一个元素中的数字值
            # （块注释参考案例）

            sys_arch = platform.architecture(executable, bits, linkage)
            self._bits = int(sys_arch[0].replace("bit", ""))
        except TypeError:  # 一般情况下不`except Exception`, 而是捕捉具体的错误类型
            # 部分Unix操作系统中的file命令实现会影响到命令执行结果
            self._bits = -1

        return self._bits
