import pprint
data = [
    {
        'pmid': 101,
        'pm_pid': 0,
        'pmname': '用户管理',
        'pmurl': None,
        'pmlevel': 0,
        'pmaction': None
    },
    {
        'pmid': 102,
        'pm_pid': 0,
        'pmname': '权限管理',
        'pmurl': None,
        'pmlevel': 0,
        'pmaction': None
    },
    {
        'pmid': 103,
        'pm_pid': 0,
        'pmname': '豆瓣电影',
        'pmurl': None,
        'pmlevel': 0,
        'pmaction': None
    },
    {
        'pmid': 101101,
        'pm_pid': 101,
        'pmname': '用户列表',
        'pmurl': 'user',
        'pmlevel': 1,
        'pmaction': None
    },
    {
        'pmid': 102101,
        'pm_pid': 102,
        'pmname': '权限列表',
        'pmurl': 'permission',
        'pmlevel': 1,
        'pmaction': None
    },
    {
        'pmid': 102102,
        'pm_pid': 102,
        'pmname': '角色列表',
        'pmurl': 'role',
        'pmlevel': 1,
        'pmaction': None
    },
    {
        'pmid': 103101,
        'pm_pid': 103,
        'pmname': 'TOP250',
        'pmurl': 'movie',
        'pmlevel': 1,
        'pmaction': None
    },
    {
        'pmid': 101101101,
        'pm_pid': 101101,
        'pmname': '查询用户',
        'pmurl': None,
        'pmlevel': 2,
        'pmaction': None
    },
    {
        'pmid': 101101102,
        'pm_pid': 101101,
        'pmname': '增加用户',
        'pmurl': None,
        'pmlevel': 2,
        'pmaction': None
    },
    {
        'pmid': 101101103,
        'pm_pid': 101101,
        'pmname': '修改用户',
        'pmurl': None,
        'pmlevel': 2,
        'pmaction': None
    },
    {
        'pmid': 101101104,
        'pm_pid': 101101,
        'pmname': '删除用户',
        'pmurl': None,
        'pmlevel': 2,
        'pmaction': None
    },
    {
        'pmid': 101101105,
        'pm_pid': 101101,
        'pmname': '分配角色',
        'pmurl': None,
        'pmlevel': 2,
        'pmaction': None
    },
]


def list_to_tree(data):
    #out = {0: {'pmid': 0, 'pm_pid': 0, 'pmname': "Root node", 'sub': []}}
    out = {}

    for p in data:
        out.setdefault(p['pm_pid'], {'sub': []})
        out.setdefault(p['pmid'], {'sub': []})
        out[p['pmid']].update(p)
        out[p['pm_pid']]['sub'].append(out[p['pmid']])

    return out[0]


tree = list_to_tree(data)

pprint.pprint(tree)
print(tree)