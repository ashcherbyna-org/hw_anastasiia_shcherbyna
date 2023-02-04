from abc import ABC, abstractmethod


class Iphone(ABC):
    def __init__(self, model, memory_size, display, display_size):
        self.model = model
        self.platform = "IOS"
        self.memory_size = memory_size
        self.display = display
        self.display_size = display_size
        self.__features = []

    @abstractmethod
    def iphone_model(self):
        pass

    @abstractmethod
    def iphone_memory_size(self):
        pass

    def iphone_display(self):
        print(self.display)

    @abstractmethod
    def iphone_display_size(self):
        pass

    def _add_feature(self, feature):
        self.__features.append(feature)

    def _print_platform(self, version):
        print(f"{self.platform} {version}")

    def print_features(self):
        print(self.__features)


class Iphone11(Iphone):
    def __init__(self, memory_size, display_size):
        super().__init__("is 11 iphone", memory_size, "Retina", display_size)
        self.__esim()

    def iphone_model(self):
        print(f"This {self.model}")

    def iphone_memory_size(self):
        print(f"Size is {self.memory_size}")

    def iphone_display_size(self):
        print(f"Display size is {self.display_size}")

    def print_platform_version(self):
        super()._print_platform("15")

    def __esim(self):
        super()._add_feature("esim")


class Iphone12(Iphone):
    def __init__(self, memory_size, display_size):
        super().__init__("is 12 iphone", memory_size, "Retina", display_size)
        self.__touch_screenshot()

    def iphone_model(self):
        print(f"This {self.model}")

    def iphone_memory_size(self):
        print(f"Size is {self.memory_size}")

    def iphone_display_size(self):
        print(f"Display size is {self.display_size}")

    def print_platform_version(self):
        super()._print_platform("16")

    def __touch_screenshot(self):
        super()._add_feature("touch screenshot")


if __name__ == "__main__":
    iphone11 = Iphone11("64 GB", "6.06")
    iphone11.iphone_display_size()
    iphone11.iphone_memory_size()
    iphone11.iphone_model()
    iphone11.iphone_display()
    iphone11.print_features()
    iphone11.print_platform_version()

    iphone12 = Iphone12("128 GB", "6.06")
    iphone12.iphone_display_size()
    iphone12.iphone_memory_size()
    iphone12.iphone_model()
    iphone12.iphone_display()
    iphone12.print_features()
    iphone12.print_platform_version()