async def get_link_token(email_with_link):
    link_start = email_with_link.find('set-password\/') + 14
    link_end = link_start + 32
    token = email_with_link[link_start: link_end]
    return token
