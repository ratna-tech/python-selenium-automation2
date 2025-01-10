# Created by ashva at 12/8/2024
Feature: Target help features
  # Enter feature description here

  Scenario: verify target help page
    Given Open Target help page
    Then verify Target Help is present
    Then verify Search Help textbox
    Then verify Search Help button
    Then verify 6 grids under What would you like to do
    Then verify grids in What would you like to do footer
  #  Then verify Browse all Help pages


  Scenario: Verify help topic dropdown
    Given Open Target help subcategory page
    When Select help topic dropdown
    Then Verify Returns page opens