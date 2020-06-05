import pytest
from Page.searchPage import SearchPage
from Base.driver import Driver


class TestSearch:

    def setup_class(self):
        """声明driver"""
        # 实例化页面类
        self.sp_obj = SearchPage()

    def teardown_class(self):
        """退出driver"""
        # 引用自定义driver类的退出方法
        Driver.quit_app_driver()

    @pytest.fixture(scope="class", autouse=True)  # 因为只点击一次搜索按钮 自动运行
    def click_search_btn(self):
        """点击搜索按钮 1次 输入之前运行"""
        # 点击搜索
        self.sp_obj.click_search_btn()

    @pytest.mark.parametrize("search_text,search_result", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search(self, search_text, search_result):
        """内容输入 和 结果断言"""
        # 输入框
        self.sp_obj.send_search_text(search_text)

        # 断言 -列表式断言
        assert search_result in self.sp_obj.get_search_result()
