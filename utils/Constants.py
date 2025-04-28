
class AppConstants:
    PAGE_HEADINGS = {
        "newsletterSubscription": "Become a newsletter subscriber",
        "myAccount": "My Account"
    }

    STATUS_CODES = {
        "success": 200,
        "not_found": 404,
        "server_error": 500
    }

    ERROR_MESSAGES = {
        "invalid_Captcha_error": "Human verification has failed! Please try agan.",
        "invalidLogin": "Error: Incorrect login or password provided."
    }

    TIMEOUTS = {
        "short": 5000,
        "medium": 10000,
        "long": 30000,
    }