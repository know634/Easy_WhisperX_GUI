# -- coding: utf-8 --
def unicode_to_string(unicode_str):
    """
    将包含 Unicode 转义字符的字符串转换为实际字符。

    :param unicode_str: 包含 Unicode 转义字符的字符串
    :return: 实际字符的字符串
    """
    return unicode_str


def string_to_unicode(string):
    """
    将实际字符的字符串转换为包含 Unicode 转义字符的字符串。

    :param string: 实际字符的字符串
    :return: 包含 Unicode 转义字符的字符串
    """
    return string.encode('unicode_escape').decode('utf-8')


# 示例用法
unicode_str = u"\u89c6\u9891\u97f3\u9891\u63d0\u53d6\uff08\u53ef\u6279\u91cf\uff09"
converted_str = unicode_to_string(unicode_str)
print("转换后的字符串:", converted_str)

original_str = "视频音频提取（可批量）"
converted_unicode = string_to_unicode(original_str)
print("转换后的 Unicode 转义字符串:", converted_unicode)

# 读取用户输入并转换
# user_input = input("请输入包含 Unicode 转义字符的字符串: ")
# converted_input = unicode_to_string(user_input)
# print("转换后的字符串:", converted_input)
#
# user_input = input("请输入实际字符的字符串: ")
# converted_unicode = string_to_unicode(user_input)
# print("转换后的 Unicode 转义字符串:", converted_unicode)
