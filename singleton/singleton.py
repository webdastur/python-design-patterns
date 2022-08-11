class SingleObject:
    _instance: "SingleObject"

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingleObject, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls) -> "SingleObject":
        return cls()

    def show_message(self):
        print("Hello World!")


if __name__ == "__main__":
    single_object = SingleObject.get_instance()
    single_object.show_message()
