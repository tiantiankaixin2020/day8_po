from selenium.webdriver.common.by import By

from Base.base import Base
from Page.pageElement import PageElement


class SearchPage(Base):

    def __init__(self):
        # 实例化Base类
        Base.__init__(self)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageElement.search_btn)

    def send_search_text(self, text):
        """
        输入搜索内容
        :param text: 需要输入的搜索内容
        :return:
        """
        self.send_ele(PageElement.search_input, text)

    def get_search_result(self):
        """获取搜索结果"""
        # 返回定位对象列表目的？？[对象1, 对象2.....] -> [对象1文本，对象2文本....]
        results = self.search_eles(PageElement.search_result)
        return [i.text for i in results]
