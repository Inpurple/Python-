def BubbleSort(List):
    """
    1.1 冒泡排序(Bubble Sort)
    比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    针对所有的元素重复以上的步骤，除了最后一个；
    重复步骤1~3，直到排序完成。
    冒泡排序对n个数据操作n-1轮，每轮找出一个最大（小）值。

    操作只对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。

    每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

    额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)
    """
    n=len(List)
    for i in range(n-1,0,-1):#将最大的数排到最后面去
        for j in range(0,i):#每一轮冒泡进行相邻线的数对比，大的排在后面
            if List[j]>List[j+1]:
                List[j+1],List[j]=List[j],List[j+1]
                
    return List