import html
import gradio as gr
import baidu_translate as fanyi

params = {
    "activate": True,
    "language string": "zh",
}

language_codes = {'自动检测': 'auto', '中文(简体)': 'zh', '英语': 'en', '西班牙语': 'spa', '阿拉伯语': 'ara',
                  '法语': 'fra', '俄语': 'ru', '日语': 'jp', '泰语': 'th', '韩语': 'kor', '德语': 'de',
                  '葡萄牙语': 'pt', '意大利语': 'it', '希腊语': 'el', '荷兰语': 'nl', '波兰语': 'pl', '芬兰语': 'fin',
                  '捷克语': 'cs', '保加利亚语': 'bul', '丹麦语': 'dan', '爱沙尼亚语': 'est', '匈牙利语': 'hu',
                  '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo', '瑞典语': 'swe', '越南语': 'vie', '中文(粤语)': 'yue',
                  '中文(繁体)': 'cht', '中文(文言文)': 'wyw', '南非荷兰语': 'afr', '阿尔巴尼亚语': 'alb',
                  '阿姆哈拉语': 'amh', '亚美尼亚语': 'arm', '阿萨姆语': 'asm', '阿斯图里亚斯语': 'ast',
                  '阿塞拜疆语': 'aze', '巴斯克语': 'baq', '白俄罗斯语': 'bel', '孟加拉语': 'ben', '波斯尼亚语': 'bos',
                  '缅甸语': 'bur', '加泰罗尼亚语': 'cat', '宿务语': 'ceb', '克罗地亚语': 'hrv', '世界语': 'epo',
                  '法罗语': 'fao', '菲律宾语': 'fil', '加利西亚语': 'glg', '格鲁吉亚语': 'geo', '古吉拉特语': 'guj',
                  '豪萨语': 'hau', '希伯来语': 'heb', '印地语': 'hi', '冰岛语': 'ice', '伊博语': 'ibo', '印尼语': 'id',
                  '爱尔兰语': 'gle', '卡纳达语': 'kan', '克林贡语': 'kli', '库尔德语': 'kur', '老挝语': 'lao',
                  '拉丁语': 'lat', '拉脱维亚语': 'lav', '立陶宛语': 'lit', '卢森堡语': 'ltz', '马其顿语': 'mac',
                  '马拉加斯语': 'mg', '马来语': 'may', '马拉雅拉姆语': 'mal', '马耳他语': 'mlt', '马拉地语': 'mar',
                  '尼泊尔语': 'nep', '新挪威语': 'nno', '波斯语': 'per', '萨丁尼亚语': 'srd',
                  '塞尔维亚语(拉丁文)': 'srp', '僧伽罗语': 'sin', '斯洛伐克语': 'sk', '索马里语': 'som',
                  '斯瓦希里语': 'swa', '他加禄语': 'tgl', '塔吉克语': 'tgk', '泰米尔语': 'tam', '鞑靼语': 'tat',
                  '泰卢固语': 'tel', '土耳其语': 'tr', '土库曼语': 'tuk', '乌克兰语': 'ukr', '乌尔都语': 'urd',
                  '奥克语': 'oci', '吉尔吉斯语': 'kir', '普什图语': 'pus', '高棉语': 'hkm', '海地语': 'ht',
                  '书面挪威语': 'nob', '旁遮普语': 'pan', '阿尔及利亚阿拉伯语': 'arq', '比斯拉马语': 'bis',
                  '加拿大法语': 'frn', '哈卡钦语': 'hak', '胡帕语': 'hup', '印古什语': 'ing', '拉特加莱语': 'lag',
                  '毛里求斯克里奥尔语': 'mau', '黑山语': 'mot', '巴西葡萄牙语': 'pot', '卢森尼亚语': 'ruy',
                  '塞尔维亚-克罗地亚语': 'sec', '西里西亚语': 'sil', '突尼斯阿拉伯语': 'tua', '亚齐语': 'ach',
                  '阿肯语': 'aka', '阿拉贡语': 'arg', '艾马拉语': 'aym', '俾路支语': 'bal', '巴什基尔语': 'bak',
                  '本巴语': 'bem', '柏柏尔语': 'ber', '博杰普尔语': 'bho', '比林语': 'bli', '布列塔尼语': 'bre',
                  '切罗基语': 'chr', '齐切瓦语': 'nya', '楚瓦什语': 'chv', '康瓦尔语': 'cor', '科西嘉语': 'cos',
                  '克里克语': 'cre', '克里米亚鞑靼语': 'cri', '迪维希语': 'div', '古英语': 'eno', '中古法语': 'frm',
                  '弗留利语': 'fri', '富拉尼语': 'ful', '盖尔语': 'gla', '卢干达语': 'lug', '古希腊语': 'gra',
                  '瓜拉尼语': 'grn', '夏威夷语': 'haw', '希利盖农语': 'hil', '伊多语': 'ido', '因特语': 'ina',
                  '伊努克提图特语': 'iku', '爪哇语': 'jav', '卡拜尔语': 'kab', '格陵兰语': 'kal', '卡努里语': 'kau',
                  '克什米尔语': 'kas', '卡舒比语': 'kah', '卢旺达语': 'kin', '刚果语': 'kon', '孔卡尼语': 'kok',
                  '林堡语': 'lim', '林加拉语': 'lin', '逻辑语': 'loj', '低地德语': 'log', '下索布语': 'los',
                  '迈蒂利语': 'mai', '曼克斯语': 'glv', '毛利语': 'mao', '马绍尔语': 'mah', '南恩德贝莱语': 'nbl',
                  '那不勒斯语': 'nea', '西非书面语': 'nqo', '北方萨米语': 'sme', '挪威语': 'nor', '奥杰布瓦语': 'oji',
                  '奥里亚语': 'ori', '奥罗莫语': 'orm', '奥塞梯语': 'oss', '邦板牙语': 'pam', '帕皮阿门托语': 'pap',
                  '北索托语': 'ped', '克丘亚语': 'que', '罗曼什语': 'roh', '罗姆语': 'ro', '萨摩亚语': 'sm',
                  '梵语': 'san', '苏格兰语': 'sco', '掸语': 'sha', '修纳语': 'sna', '信德语': 'snd', '桑海语': 'sol',
                  '南索托语': 'sot', '叙利亚语': 'syr', '德顿语': 'tet', '提格利尼亚语': 'tir', '聪加语': 'tso',
                  '契维语': 'twi', '高地索布语': 'ups', '文达语': 'ven', '瓦隆语': 'wln', '威尔士语': 'wel',
                  '西弗里斯语': 'fry', '沃洛夫语': 'wol', '科萨语': 'xho', '意第绪语': 'yid', '约鲁巴语': 'yor',
                  '扎扎其语': 'zaz', '祖鲁语': 'zul', '巽他语': 'sun', '苗语': 'hmn', '塞尔维亚语(西里尔文)': 'src'}


def input_modifier(string):
    """
    This function is applied to your text inputs before
    they are fed into the model.
    """
    if not params['activate']:
        return string

    return fanyi.translate_text(string, from_=fanyi.Lang.AUTO, to=fanyi.Lang.EN)


def output_modifier(string):
    """
    This function is applied to the model outputs.
    """
    if not params['activate']:
        return string
    return fanyi.translate_text(html.unescape(string), from_='en', to=params['language string'])


def bot_prefix_modifier(string):
    """
    This function is only applied in chat mode. It modifies
    the prefix text for the Bot and can be used to bias its
    behavior.
    """

    return string


def ui():
    # Finding the language name from the language code to use as the default value
    language_name = list(language_codes.keys())[list(language_codes.values()).index(params['language string'])]

    # Gradio elements
    with gr.Row():
        activate = gr.Checkbox(value=params['activate'], label='启用翻译')

    with gr.Row():
        language = gr.Dropdown(value=language_name, choices=[k for k in language_codes], label='AI的语言')

    # Event functions to update the parameters in the backend
    activate.change(lambda x: params.update({"activate": x}), activate, None)
    language.change(lambda x: params.update({"language string": language_codes[x]}), language, None)
