def test_successful_login(login_page, valid_user):
    """
    1. Navigate to base url
    2. Enter 'standard_user' as username
    3. Enter 'secret_sauce' as password
    4. Click Login button.
    Verify that Inventory page is displayed
    """
    inventory_page = login_page.successful_login(valid_user)
    assert inventory_page.is_page_displayed()


def test_locked_out_login(login_page, locked_out_user):
    login_page.unsuccessful_login(locked_out_user)

    assert login_page.login_button.is_displayed()

    assert login_page.error_message.is_displayed()
    assert login_page.error_message.text == 'Epic sadface: Sorry, this user has been locked out.'

    assert login_page.username_error_marker.is_displayed()
    assert login_page.password_error_marker.is_displayed()
