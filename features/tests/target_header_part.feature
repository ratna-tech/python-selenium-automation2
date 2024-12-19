# Created by ashva at 12/19/2024
Feature: Target header features
  # Enter feature description here

 Scenario: User can sign into target account
    Given Open Target page
    When Click Sign In
    When From right side navigation menu, click Sign
    When Enter email
    When Enter password
    When Click on Signin button
    #When Click on Maybe later button
    When Click skip button
    Then Verify Sign in
