import get_session as get_session

session = get_session.get_session()

def get_cookies(session):
    cookies = dict(session.get("https://discord.com/api/v9/experiments").cookies)
    cookies["__cf_bm"]="0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="
    cookies["locale"]="ja-JP"
    return cookies
