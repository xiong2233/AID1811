# 扑克牌，只取红方花色13，用数字1-13表示
#13张牌从小到大排序，反面朝上，查找红方9
#问题2：使用二分法查找，使用Python实现该过程
   
# def binary(value,key,left,right):
#     if left > right:
#         return-1
#     #获取中间元素对应下标
#     middle = (left+right)//2
#     #对比中间元素值与指定值
#     #如果相同
#     if value[middle] == key:
#         #查找成功，返回对应下标
#         return middle
#     #如果指定值小于中间值
#     elif value[middle] > key:
#         #则在左侧继续查找
#         #查找范围减半，左侧下标值不变
#         #而右侧下标值为中间值的前一侧
#         return binary(value,key,left,middle-1)
#     else:
#         #则在右侧继续查找
#         #查找范围减半，右侧下标值不变
#         #而左侧下标值为中间值最后的位置
#         return binary(value,key,middle+1,right)
# if __name__ == "__main__":
#     #原始数据 -有序
#     value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     #待查找数据
#     key = 9
#     #二分法
#     res = binary(value,key,0,len(value)-1)
#     if res == -1:
#         print("未查找到")
#     else:
#         print("下标值为：",res)



value = range(1,101)
s = len(value)-1
for i in range(s):
    if value[s] == 9:
        print("下标为：",s)
        break
    elif value[s] > 9:
        s -= (len(value[0:s])-1)//2
    elif value[s] < 9:
        s +=(len(value[s:(len(value)-1)])-1)//2

        
        


