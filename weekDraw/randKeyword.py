#這是一個從自己建設好的關鍵字列表中隨機抽取數個關鍵字的功能
import random
# print(random.random())
# print(random.uniform(1,10))
# print(rd.randint())
# print(random.randrange(10))#0~9 int



def randPick():
    colorK = ["red","blue","green","black","white",'yellow',"pink","gray"]
    genderK = ["female","male","no gender"]
    ageK = ["0~10","11~15","16~20","20~30","30~40","40up"]

    colorV = colorK[random.randrange(8)]
    genderV = genderK[random.randrange(3)]
    ageV = ageK[random.randrange(6)]

    return colorV,genderV,ageV


if __name__ == '__main__' :
    c,g,a = randPick()
    print(c)
    print(g)
    print(a)
