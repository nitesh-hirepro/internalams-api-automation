login_server = input('server_name :: beta or live ')

generic_domain = ''

if login_server == 'beta':
    generic_domain = 'https://beta-internalams.hirepro.in/py/'
else:
    generic_domain = 'https://internalams.hirepro.in/py/'

apis = {
    "get_tenant_details":   generic_domain + 'common/get_tenant_details/',
    "login_to_internalams": generic_domain + 'common/user/v2/login_user/',
    "get_impact_data": generic_domain + 'oneams/impact/get_all_time_sheets/',
    "create_impact": generic_domain + 'oneams/impact/create_update_time_sheet/',
    "search_impact": generic_domain + 'oneams/impact/get_all_time_sheets/'
}