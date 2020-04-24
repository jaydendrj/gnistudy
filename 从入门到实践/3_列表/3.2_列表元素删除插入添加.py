invite_list=['a','xiaoming','3','dj']
busy_friend='3'
l=busy_friend+'不能参加。'
print(l)
invite_list.remove(busy_friend)
new_fiend='ne'
invite_list.append(new_fiend)    #没办法替换到原来的位置，怎么通过元素找到对应的索引值（虽然元素不唯一（可能重复出现））
message=invite_list[0]+",一起吃晚饭。"
print(message)
print('我找到了一个更大的餐桌。')
invite_list.insert(0,'cm')
invite_list .insert(2,'dkj')   #中间具体那里，随便指定
invite_list.append('sadf')
message=invite_list[0]+'一起吃晚饭。'
print(message)
print('只能邀请两人。')
miss_friend=invite_list .pop(1)
message=miss_friend+',抱歉不能一起吃晚饭。'
print(message)
miss_friend=invite_list .pop(1)
message=miss_friend+',抱歉不能一起吃晚饭。'
print(message)
print(invite_list)
miss_friend=invite_list .pop(1)
message=miss_friend+',抱歉不能一起吃晚饭。'
print(message)
miss_friend=invite_list .pop(1)
message=miss_friend+',抱歉不能一起吃晚饭。'
print(message)
miss_friend=invite_list .pop(1)
message=miss_friend+',抱歉不能一起吃晚饭。'
print(message)

print(invite_list)
message=invite_list[0]+',一起吃晚饭。'
print(message)
message=invite_list[1]+',一起吃晚饭。'
print(message)
l=len(invite_list)
message='一共邀请了'+str(l)+'个朋友。'
print(message)
del invite_list[0]
print(invite_list)
del invite_list[0]
print(invite_list)
