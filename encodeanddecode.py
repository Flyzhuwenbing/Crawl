import sys
print(sys.getdefaultencoding())
s = "你好"
print(s)
s1 = s.encode("gbk").decode("gbk")
print(s1)