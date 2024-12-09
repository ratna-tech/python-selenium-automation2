Feature: Test Scenarios for Search functionality

  Scenario: # Search for candy
    Given Open Target page
    When search for candy
    When add item to cart
    Then verify item in cart

Scenario: # Search for airpods
    Given Open Target page
    When search for airpods
    When add item to cart
    Then verify item in cart