# Created by ashva at 12/7/2024
Feature: target main page features
  # Enter feature description here

Scenario: User can go to sign in page
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign
    Then Verify Sign into your Target account is shown

 """Scenario: User can sign into target account
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign
    When Enter email
    When Enter password
    When Click on Signin button
    #When Click on Maybe later button
    When Click skip button
    Then Verify Sign in"""
