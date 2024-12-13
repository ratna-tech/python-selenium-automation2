# Created by ashva at 12/8/2024
Feature:target cart featurres
  # Enter feature description here

 Scenario: verify item in cart
    Given Open Target page
    When search for candy
    When add item to cart
    Then verify item in cart