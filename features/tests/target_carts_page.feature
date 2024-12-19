# Created by ashva at 12/8/2024
Feature:target cart featurres
  # Enter feature description here

 Scenario: verify item in cart
    Given Open Target page
    When search for jeans
    When add item to cart
    Then verify jeans in cart

Scenario: Verify Your cart is empty message displays
    Given Open Target page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown