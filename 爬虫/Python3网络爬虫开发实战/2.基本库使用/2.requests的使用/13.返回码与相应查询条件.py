# 返回码与相应的查询条件
# 信息性状态码
code_info = {
    100: 'continue',
    101: 'switchin_protocols',
    102: 'processing',
    103: 'checkpoint',
    122: ('uri_too_long', 'request_uri_too_long')
}

# 成功状态码
code_success = {
    200: ('ok', 'okay', 'all_ok', 'all_good', '\\o/', '√'),
    201: 'created',
    202: 'accepted',
    203: ('non_authoritative_info', 'no_authoritative_information'),
    204: 'no_content',
    205: ('reset_content', 'reset'),
    206: ('partial_content', 'partial'),
    207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
    208: 'already_reported',
    226: 'im_used',
}