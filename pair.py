class DataHelper:

    def __init__(self):
        self.data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
    
    def show_data(self):
      for index, item in enumerate(self.data):
          print(f"Item {index + 1}: {item}")



helper = DataHelper()

helper.show_data()