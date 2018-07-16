
'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

'''
nums = {
'0':'',
'1':'one',
'2':'two',
'3':'three',
'4':'four',
'5':'five',
'6':'six',
'7':'seven',
'8':'eight',
'9':'nine',
'10':'ten',
'11':'eleven',
'12':'twelve',
'13':'thirteen',
'14':'fourteen',
'15':'fifteen',
'16':'sixteen',
'17':'seventeen',
'18':'eighteen',
'19':'nineteen',
'20':'twenty',
'30':'thirty',
'40':'forty',
'50':'fifty',
'60':'sixty',
'70':'seventy',
'80':'eighty',
'90':'ninety'
}

def lettersInNum(val):
    strVal = str(val)
    parts = len(strVal)

    if parts == 3:
        part3 = (nums[strVal[0]])
        part3 = part3 + ('hundred')

        if int(strVal[1:len(strVal)]) < 20:
            if int(strVal[1:len(strVal)]) == 0:
                part2 = ''
                part1 = ''
            else:
                part2 = 'And' + (nums[str(int(strVal[1:len(strVal)]))])
                part1 = ''

        else:
            part2 =  'And' + (nums[str(int(strVal[1])*10)])
            part1 = (nums[strVal[2]])

        print((part3 + part2 + part1))
        return len(part3 + part2 + part1)

    elif parts == 2:
        if int(strVal[0:len(strVal)]) < 20:
            part2 = (nums[str(int(strVal[0:len(strVal)]))])
            part1 = ''

        else:
            part2 = (nums[str(int(strVal[0])*10)])
            part1 = (nums[strVal[1]])

        print(( part2 + part1))
        return len(part2 + part1)

    elif parts == 1:
        part1 = (nums[strVal[0]])

        print((part1))
        return len(part1)

#onethousand
tot = len('onethousand')
for val in range(1,1000):
    tot = tot + lettersInNum(val)

print(tot)

































