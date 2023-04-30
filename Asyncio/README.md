Asyncio
=====
* ### 加速篇: Python 的 Numba 庫 (從爬不太動到原地起飛)
* ### Chapter1 Python AIO 庫
* ### Chapter2 Docker 工具
* ### Chapter3 AIOHTTP
* ### Chapter4 aioMySQL
* ### Chapter5 ASGI
* ### Chapter6 Tornado
* ### Chapter7 Socket.IO
<br />

加速篇: Python 的 Numba 庫 (從爬不太動到原地起飛)
=====
* ### Numba 通过使用 LLVM 技术，将 Python 代码编译生成优化后的机器码，可以大幅提高代码执行效率。
* ### 针对 Python 加速，可以使用多线程與多进程，而更有效果的是 Numba，官网对它的定位是 "一个Python 编译器"。
* ### Numba 是一个源于 Anaconda 的 Python 编译器，可以在支持 CUDA 的 GPU 上编译 Python 可执行代码。
* ### Numba 给 Python 开发者提供了一个简单入门 GPU 加速计算的方式，以及学习最少新语法、术语就可以使用日益复杂的 CUDA 代码的捷径。
* ### Numba 是一个实时、类型专门化的函数编译器，用于加速以数字计算为重点的 Python 编程。
* ### Numba 不仅仅可以实现 GPU 加速，还可以利用多核 CPU 实现加速，在某些没有 GPU 或者不支持 CUDA 的 GPU 电脑上，Numba 依旧可以充分利用 CPU 的计算能力提升效率。
* ### Numba reads the Python bytecode for a decorated function and combines this with information about the types of the input arguments to the function. It analyzes and optimizes your code, and finally uses the LLVM compiler library to generate a machine code version of your function, tailored to your CPU capabilities. This compiled version is then used every time your function is called.
* ### 一句话总结: 使用 Numba 最简单的方式就是在函数定义前加 \@jit。
* ### Numba的优势
    * ### 简单，1 行代码就有惊喜。
    * ### 对循环 (loop) 有奇效，而往往在科学计算中限制 python 速度的就是 loop。
    * ### 兼容常用的科学计算包，如 numpy、cmath 等。
    * ### 会自动调整精度，保证准确性。
* ### Numba 的 \@jit 有两种编译模式: nopython 和 object 模式。
    * ### nopython 模式会完全编译这个被修饰的函数，函数的运行与 Python 解释器完全无关，不会调用 Python 的 C 语言 API。如果想获得最佳性能，推荐使用此种模式。
    * ### object 模式中编译器会自动识别函数中循环语句等可以编译加速的代码部分，并编译成机器码，对于剩下不能识别的部分交给 Python 解释器运行。如果想获取最佳性能，避免使用这种方法。
* ### 如果没设置参数 nopython=True，Numba 首先会尝试使用 nopython 模式，如果因为某些原因无法使用，则会使用 object 模式。加了 nopython 后则会强制编译器使用 nopython 模式，但如果代码出现了不能自动推导的类型，有报错的风险 (在使用 jit 时建議明确写出 nopython=True，如果遇到问题，就解決它)。
* ### 如果真的很懶得補上 nopython=True 的話，就用 \@njit 吧 (一樣的效果，不過到底是多懶)。
```
@jit(nopython=True)
def func():
    pass
```
* ### Numba 对于 jit 也提供了参数，叫做 function signature，通过在 jit 后指定函数的输入输出数据类型，可以获得轻微的速度提升，因为编译器不需要在编译的时候自动推导类型了，坏处就是函数不能再接受其它类型的数据了。
```
@jit(float64(int32, int32))
def f(x, y):
    return (x + y) / 3.14
```
* ### jit 后面的就是 function signature。float64 表示输出数据类型，int32 表示输入数据类型 (可以简写成 "@jit(f8(i4,i4))")，如果输入输出参数是矩阵类型，则用 ":" 表示维度，二维的 float32 矩阵表示为 float32[:,:] (可以简写为 "f4[:,:]")。
* ### If your code is numerically orientated (does a lot of math), uses NumPy a lot and/or has a lot of loops, then Numba is often a good choice.
* ### Numba 在第一次运行你写的代码时会即时编译，编译会消耗一定的时间，编译好之后 Numba 会将机器码先缓存起来，第二次再调用的时候就不会再编译而是直接运行了，这与 Numba 的运行原理有关。
* ### Assuming Numba can operate in nopython mode, or at least compile some loops, it will target compilation to your specific CPU. Speed up varies depending on application but can be one to two orders of magnitude.
* ### Numba 不支援許多的第三方 package,因為 numba 主軸在於加速數據的運算，而非做資料的清理或者篩選，因此在若是程式當中有使用到第三方套件的，那建議拉出來做，只把最核心的數據運算交給 numba 加速。
* ### Numba 对没有循环或者只有非常小循环的函数加速效果并不明显，用不用都一样。
* ### Numba 还支持很多加速类型
    * ### ​\@jit(nopython=True,fastmath=True) 牺牲一丢丢数学精度来提高速度
    * ### \@jit(nopython=True,parallel=True) 自动进行并行计算
<br />

Reference
=====
* ### Python 異步編程實戰 — 基於 AIO 的全棧開發技術
<br />
