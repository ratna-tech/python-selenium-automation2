# Created by ashva at 12/21/2024
Feature: Target Terms And Conditions Feature
  #
  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   When Store original window
   And Click on Target terms and conditions link
   And Switch to the newly opened window
   Then Verify Terms and Conditions page is opened
   And User can close new window
   And switch back to original page

