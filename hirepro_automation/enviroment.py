login_server = input('server_name :: beta-internalams or internalams or amsin or beta or ams ')
sprint_version = input('sprint_version: 193 or 194 ')

generic_domain = ''

if login_server == 'beta-internalams':
    generic_domain = 'https://beta-internalams.hirepro.in/py/'
elif login_server == 'internalams':
    generic_domain = 'https://internalams.hirepro.in/py/'
elif login_server == 'amsin':
    generic_domain = 'https://amsin.hirepro.in/py/'
elif login_server == 'beta':
    generic_domain = 'https://betaams.hirepro.in/py/'
else:
    generic_domain = 'https://ams.hirepro.in/py/'

apis = {
    "get_tenant_details":   generic_domain + 'common/get_tenant_details/',
    "login_to_internalams": generic_domain + 'common/user/v2/login_user/',
    "get_impact_data": generic_domain + 'oneams/impact/get_all_time_sheets/',
    "create_impact": generic_domain + 'oneams/impact/create_update_time_sheet/',
    "search_impact": generic_domain + 'oneams/impact/get_all_time_sheets/',
    "get_all_time_sheet_entrys": generic_domain + 'oneams/impact/get_all_time_sheet_entrys/',
    "submit_impact": generic_domain + 'oneams/impact/submit_time_sheet/',
    "bulk_create_impact": generic_domain + 'oneams/impact/bulk_create_timesheet/',
    "approve_time_sheet": generic_domain + 'oneams/impact/approve_time_sheet/',
    "request_to_improve_timesheets": generic_domain + 'oneams/impact/request_to_remove_timesheets/',
    "accept_remove_requests": generic_domain + 'oneams/impact/accept_remove_requests/',
    "get_all_sources": generic_domain + 'rpo/get_all_sources/',
    "create_source": generic_domain + 'rpo/create_source/',
    "update_source": generic_domain + 'rpo/update_source/',
    "archive_source": generic_domain + 'rpo/archive_sources/',
    "unarchive_source": generic_domain + 'rpo/unarchive_sources/',
    "extract_resume":  generic_domain + 'rpo/extract_resume_from_file_content/'
}
