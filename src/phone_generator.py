# coding:utf-8



class PhoneGenerator(object):

    # 读取文件获得手机号码段
    def read_file(self, file_path):
        phone_sections = []
        with open(file_path, 'r') as f:
            for line in f.readlines():
                phone_section = line.strip('\r\n ')
                phone_sections.append(phone_section)
        return phone_sections

    def generate_phones(self, phone_section):
        phones = []
        count = len(phone_section)
        number = 10**(11-count)
        default_number = long(phone_section) * number
        for i in xrange(0, number):
            phone = default_number + i
            phones.append(phone)
        return phones


    # 从文件获得号码段,并导入到mongo数据库,获得每个号码段导入数据数目
    def import_from_file(self, file_path):
        phone_sections = self.read_file(file_path)
        if phone_sections is None or len(phone_sections) == 0:
            return None
        phones = []
        for section in phone_sections:
            phones += self.generate_phones(section)
        return phones



