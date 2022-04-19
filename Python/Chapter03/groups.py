__author__ = "ChiangWei"
__date__ = "2022/04/19"

import sys

admins = {'Justin', 'caterpillar'}
users = set(sys.argv[1:])
# 交集
print('站長：{}'.format(admins & users))
# 減集
print('非站長：{}'.format(users - admins))
# 聯集
print('全部使用者：{}'.format(admins | users))
# 互斥
print('身份不重複使用者：{}'.format(admins ^ users))

print('站長群包括使用者群？{}'.format(admins > users))
print('使用者群包括站長群？{}'.format(admins < users))
