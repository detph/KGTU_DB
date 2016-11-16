from Widgets.ListView import MYListView


class BaseUIList(MYListView):
    # SIGNALS



    def __init__(self, parent=None):
        super(BaseUIList, self).__init__(parent=parent)

        self.__init_Attributes()
        self.__init_Parameters()


    # inits
    def __init_Attributes(self):
        pass

    def __init_Parameters(self):
        pass



