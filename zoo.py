from abc import ABC, abstractmethod


class Animal(ABC):
    """
    动物抽象类，不允许实例化
    """

    @abstractmethod
    def __init__(self, type_, size, character):
        """
        :param type_: str, 类型，如'食肉'、'食草'、'杂食'
        :param size: str, 体型，如'大'、'中'、'小'
        :param character: str, 性格，如'温顺'、'凶猛'
        """
        self.type = type_
        self.size = size
        self.character = character

    @property
    def is_ferocious(self):
        """
        是否属于凶猛动物
        :return: bool
        """
        if self.type == '食肉' and self.size in ('大', '中') and self.character == '凶猛':
            return True
        return False

    def __str__(self):
        return self.__class__.__name__


class Cat(Animal):
    """ 猫类 """

    sound = '喵喵喵'

    def __init__(self, name, type_, size, character):
        """
        :param name: str, 名字
        :param type_: str, 类型，如'食肉'、'食草'、'杂食'
        :param size: str, 体型，如'大'、'中'、'小'
        :param character: str, 性格，如'温顺'、'凶猛'
        """
        super(Cat, self).__init__(type_, size, character)
        self.name = name
        self.is_pet = True  # 是否适合做宠物，除了凶猛的都适合
        if self.is_ferocious:
            self.is_pet = False


class Zoo:
    """ 动物园类 """

    def __init__(self, name):
        """
        :param name: str, 名字
        """
        self.name = name
        self.animals = {}  # 存放动物，{类名: set()}

    def add_animal(self, animal):
        """
        添加动物
        :param animal: Animal, 具体的动物实例
        :return:
        """
        self.animals.setdefault(str(animal), set()).add(animal)

    def __getattr__(self, item):
        if self.animals.get(item):
            return True
        return False


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    pass
