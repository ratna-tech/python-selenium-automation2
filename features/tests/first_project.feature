# Created by ashva at 12/5/2024
Feature: Target Website
  # Enter feature description here

  Scenario: User can go to cart
    Given Open Target page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown

  Scenario: User can go to sign in page
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign
    Then Verify Sign into your Target account is shown




