class Check_final_data:
    def __init__(self,number=None , list_website_1=None, list_website_2=None, list_website_3=None, list_website_4=None, list_website_5=None, list_website_6=None, list_website_7=None):
        self.number = number
        self.list_1 = list_website_1
        self.list_2 = list_website_2
        self.list_3 = list_website_3
        self.list_4 = list_website_4
        self.list_5 = list_website_5
        self.list_6 = list_website_6
        self.list_7 = list_website_7
    def result(self):
        list = [self.list_1, self.list_2, self.list_3, self.list_4, self.list_5, self.list_6, self.list_7]
        count = 0
        check_data = []
        for check in list[0]:
            if self.number == 1:
                value = list[0][count]
            elif self.number == 2:
                value = list[0][count] + list[1][count]
            elif self.number == 3:
                value = list[0][count] + list[1][count] + list[2][count]
            elif self.number == 4:
                value = list[0][count] + list[1][count] + list[2][count] + list[3][count]
            elif self.number == 5:
                value = list[0][count] + list[1][count] + list[2][count] + list[3][count] + list[4][count]
            elif self.number == 6:
                value = list[0][count] + list[1][count] + list[2][count] + list[3][count] + list[4][count] + list[5][count]
            elif self.number == 7:
                value = list[0][count] + list[1][count] + list[2][count] + list[3][count] + list[4][count] + list[5][count] + list[6][count]
            check_data.append(value)
            count += 1
        return check_data