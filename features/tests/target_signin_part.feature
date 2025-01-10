# Created by ashva at 12/20/2024
Feature: # Enter feature name here
  # Enter feature description here
Scenario: Verify account not found message
  Given Open Target page
  When Click Sign In
  And From right side navigation menu, click Sign
  When Enter incorrect email
  And Enter incorrect password
  And Click on Signin button
  Then Verify Incorrect Sign in
