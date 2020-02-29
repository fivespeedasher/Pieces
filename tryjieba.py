import jieba
# aa=jieba.cut('IHS Markit的最新调查报告称，苹果可能会为 iPhone 和 Apple Watch的屏幕长期采用一种全新的节能背板技术，有助于延长其电池续航时间。IHS认为未来的iPhone中改用LTPO TFT（低温多晶硅氧化物）背板，从理论上估算 LTPO可以比LTPS 节省 5 ~ 15% 的功耗，从而延长 iPhone的电池续航时间。',cut_all=True)
# print('Full Mode:'+'/'.join(aa))
#
# bb=jieba.cut('IHS Markit的最新调查报告称，苹果可能会为 iPhone 和 Apple Watch的屏幕长期采用一种全新的节能背板技术，有助于延长其电池续航时间。IHS认为未来的iPhone中改用LTPO TFT（低温多晶硅氧化物）背板，从理论上估算 LTPO可以比LTPS 节省 5 ~ 15% 的功耗，从而延长 iPhone的电池续航时间。',cut_all=False)
# print('Default Mode:'+'/'.join(bb))#cut_all 默认为Faulse
#
bb=jieba.cut_for_search('IHS Markit的最新调查报告称，苹果可能会为 iPhone 和 Apple Watch的屏幕长期采用一种全新的节能背板技术，有助于延长其电池续航时间。IHS认为未来的iPhone中改用LTPO TFT（低温多晶硅氧化物）背板，从理论上估算 LTPO可以比LTPS 节省 5 ~ 15% 的功耗，从而延长 iPhone的电池续航时间。',HMM=True)
print('/'.join(bb))
print('/'.join(bb))
print('/'.join(bb))
print('/'.join(bb))


pp = 'IHS Markit的最新调查报告称，苹果可能会为 iPhone 和 Apple Watch的屏幕长期采用一种全新的节能背板技术，有助于延长其电池续航时间。'
