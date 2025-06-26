
### Author:
### Suyog Deepak Pardhi

# SauceDemo Automation Tests

### Technologies:
- Python
- Selenium
- WebDriver Manager

### Setup:

1. Clone this repo.

2. Install requirements:   
pip install selenium webdriver-manager

3. Run tests:

  python login_test.py

  python add_to_cart_test.py

  python checkout_test.py

## Challenges & Learnings

- Faced issues with dynamic element loading — used `time.sleep()` but should ideally use `WebDriverWait`.
- Identifying reliable locators was tricky; some button IDs were long or dynamic.
- Learned how to organize simple test flows into separate scripts.
