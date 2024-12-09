# Created by ashva at 12/7/2024
Feature: target main page features
  # Enter feature description here

  Scenario: # Enter scenario name here
    Given Open Target page
    When search for candy
    When add item to cart
    Then verify item in cart

    """Scenario: User can go to sign in page
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign
    Then Verify Sign into your Target account is shown
"""